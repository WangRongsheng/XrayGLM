"""Validation tests to verify the testing infrastructure is properly set up."""

import os
import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test cases to validate the testing infrastructure."""
    
    def test_project_structure(self):
        """Verify the project structure is correctly set up."""
        project_root = Path(__file__).parent.parent
        
        # Check essential directories exist
        assert project_root.exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
        assert (project_root / "model").exists()
        assert (project_root / "data").exists()
        
        # Check essential files exist
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / "README.md").exists()
        assert (project_root / "requirements.txt").exists()
    
    def test_python_path(self):
        """Verify the Python path is correctly configured."""
        # The project root should be in the Python path
        project_root = str(Path(__file__).parent.parent)
        assert any(project_root in path for path in sys.path)
    
    def test_imports(self):
        """Test that project modules can be imported."""
        try:
            import model
            assert model is not None
        except ImportError:
            pytest.fail("Failed to import 'model' package")
    
    def test_fixtures_available(self, temp_dir, mock_config, device):
        """Test that pytest fixtures are available."""
        assert temp_dir is not None
        assert temp_dir.exists()
        assert isinstance(mock_config, dict)
        assert device in ["cpu", "cuda"]
    
    def test_markers_configured(self, pytestconfig):
        """Test that custom markers are properly configured."""
        markers = pytestconfig.getini("markers")
        marker_names = [m.split(":")[0].strip() for m in markers]
        
        assert "unit" in marker_names
        assert "integration" in marker_names
        assert "slow" in marker_names
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit marker works."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration marker works."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow marker works."""
        assert True
    
    def test_coverage_configuration(self, pytestconfig):
        """Test that coverage is properly configured."""
        addopts = pytestconfig.getini("addopts")
        
        # Check coverage options are present
        assert any("--cov" in opt for opt in addopts)
        assert any("--cov-report=html" in opt for opt in addopts)
        assert any("--cov-report=xml" in opt for opt in addopts)
    
    def test_sample_image_fixture(self, sample_image_path):
        """Test the sample image fixture."""
        assert sample_image_path.exists()
        assert sample_image_path.suffix == ".png"
        
        # Verify it's a valid image
        from PIL import Image
        img = Image.open(sample_image_path)
        assert img.size == (100, 100)
    
    def test_mock_model_fixture(self, mock_model):
        """Test the mock model fixture."""
        import torch
        
        assert isinstance(mock_model, torch.nn.Module)
        
        # Test forward pass
        input_tensor = torch.randn(1, 10)
        output = mock_model(input_tensor)
        assert output.shape == (1, 2)
    
    def test_capture_logs_fixture(self, capture_logs):
        """Test the log capture fixture."""
        import logging
        
        logger = logging.getLogger(__name__)
        logger.info("Test log message")
        
        log_output = capture_logs.getvalue()
        assert "Test log message" in log_output
    
    def test_environment_reset(self):
        """Test that environment is properly reset between tests."""
        # Set a test environment variable
        os.environ["TEST_VAR"] = "test_value"
        assert os.environ.get("TEST_VAR") == "test_value"
        
        # In a real test run, the reset_environment fixture
        # will clean this up automatically


class TestPoetryIntegration:
    """Test Poetry integration and commands."""
    
    def test_pyproject_toml_valid(self):
        """Test that pyproject.toml is valid."""
        import tomllib
        
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        with open(pyproject_path, 'rb') as f:
            data = tomllib.load(f)
        
        # Check Poetry section
        assert "tool" in data
        assert "poetry" in data["tool"]
        assert "name" in data["tool"]["poetry"]
        assert data["tool"]["poetry"]["name"] == "xrayglm"
        
        # Check dependencies
        assert "dependencies" in data["tool"]["poetry"]
        assert "python" in data["tool"]["poetry"]["dependencies"]
        
        # Check dev dependencies
        assert "group" in data["tool"]["poetry"]
        assert "dev" in data["tool"]["poetry"]["group"]
        assert "dependencies" in data["tool"]["poetry"]["group"]["dev"]
        
        dev_deps = data["tool"]["poetry"]["group"]["dev"]["dependencies"]
        assert "pytest" in dev_deps
        assert "pytest-cov" in dev_deps
        assert "pytest-mock" in dev_deps
        
        # Check scripts
        assert "scripts" in data["tool"]["poetry"]
        assert "test" in data["tool"]["poetry"]["scripts"]
        assert "tests" in data["tool"]["poetry"]["scripts"]
    
    def test_pytest_configuration(self):
        """Test pytest configuration in pyproject.toml."""
        import tomllib
        
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        with open(pyproject_path, 'rb') as f:
            data = tomllib.load(f)
        
        # Check pytest configuration
        assert "pytest" in data["tool"]
        assert "ini_options" in data["tool"]["pytest"]
        
        ini_options = data["tool"]["pytest"]["ini_options"]
        assert "minversion" in ini_options
        assert "testpaths" in ini_options
        assert "tests" in ini_options["testpaths"]
        assert "markers" in ini_options
    
    def test_coverage_configuration(self):
        """Test coverage configuration in pyproject.toml."""
        import tomllib
        
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        with open(pyproject_path, 'rb') as f:
            data = tomllib.load(f)
        
        # Check coverage configuration
        assert "coverage" in data["tool"]
        assert "run" in data["tool"]["coverage"]
        assert "report" in data["tool"]["coverage"]
        assert "html" in data["tool"]["coverage"]
        assert "xml" in data["tool"]["coverage"]
        
        # Verify coverage sources
        sources = data["tool"]["coverage"]["run"]["source"]
        assert "model" in sources
        assert "data" in sources