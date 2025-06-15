import os
import sys
import tempfile
from pathlib import Path
from typing import Generator

import pytest
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config() -> dict:
    """Provide a mock configuration dictionary."""
    return {
        "model_name": "xrayglm-test",
        "batch_size": 2,
        "learning_rate": 1e-4,
        "num_epochs": 1,
        "device": "cpu",
        "checkpoint_dir": "/tmp/test_checkpoints",
        "data_dir": "/tmp/test_data",
        "log_level": "INFO",
    }


@pytest.fixture
def sample_image_path(temp_dir: Path) -> Path:
    """Create a sample image file for testing."""
    import numpy as np
    from PIL import Image
    
    image_path = temp_dir / "test_image.png"
    
    # Create a simple test image (100x100 RGB)
    img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    img = Image.fromarray(img_array)
    img.save(image_path)
    
    return image_path


@pytest.fixture
def sample_json_data() -> dict:
    """Provide sample JSON data for testing."""
    return {
        "images": [
            {
                "id": "test_001",
                "filename": "test_001.png",
                "width": 512,
                "height": 512,
            },
            {
                "id": "test_002", 
                "filename": "test_002.png",
                "width": 256,
                "height": 256,
            }
        ],
        "annotations": [
            {
                "id": 1,
                "image_id": "test_001",
                "caption": "Test X-ray showing normal chest",
                "findings": ["Normal heart size", "Clear lung fields"],
            },
            {
                "id": 2,
                "image_id": "test_002",
                "caption": "Test X-ray with abnormal findings",
                "findings": ["Enlarged heart", "Pulmonary edema"],
            }
        ]
    }


@pytest.fixture
def mock_model():
    """Create a mock model for testing."""
    class MockModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.linear = torch.nn.Linear(10, 2)
            
        def forward(self, x):
            return self.linear(x)
    
    return MockModel()


@pytest.fixture
def device() -> str:
    """Return the appropriate device for testing."""
    return "cuda" if torch.cuda.is_available() else "cpu"


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_api_response() -> dict:
    """Provide a mock API response for testing."""
    return {
        "status": "success",
        "data": {
            "prediction": "Normal chest X-ray",
            "confidence": 0.95,
            "findings": [],
        },
        "timestamp": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    import logging
    from io import StringIO
    
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Get root logger
    logger = logging.getLogger()
    original_level = logger.level
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    yield log_capture
    
    # Clean up
    logger.removeHandler(handler)
    logger.setLevel(original_level)


@pytest.fixture
def mock_gradio_interface():
    """Mock Gradio interface for web demo testing."""
    class MockGradioInterface:
        def __init__(self):
            self.launched = False
            self.inputs = []
            self.outputs = []
            
        def launch(self, **kwargs):
            self.launched = True
            self.launch_kwargs = kwargs
            return self
            
        def close(self):
            self.launched = False
    
    return MockGradioInterface()


def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)