"""
Model registry and loading utilities
"""

from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Base class for all models in the benchmark."""
    
    @abstractmethod
    def forward(self, image, text: Optional[str] = None):
        """Forward pass of the model."""
        pass
    
    @abstractmethod
    def generate(self, image, prompt: str, **kwargs):
        """Generate text response given image and prompt."""
        pass


class ModelRegistry:
    """Registry for managing different model implementations."""
    
    _models = {}
    
    @classmethod
    def register(cls, name: str, model_class):
        """Register a model class."""
        cls._models[name] = model_class
    
    @classmethod
    def get_model(cls, name: str, **kwargs):
        """Get a model instance by name."""
        if name not in cls._models:
            raise ValueError(f"Model {name} not found in registry")
        return cls._models[name](**kwargs)
    
    @classmethod
    def list_models(cls):
        """List all registered models."""
        return list(cls._models.keys())


def load_model(model_name: str, config: Optional[Dict[str, Any]] = None):
    """
    Load a model by name.
    
    Args:
        model_name: Name of the model to load
        config: Model configuration
        
    Returns:
        Model instance
    """
    config = config or {}
    return ModelRegistry.get_model(model_name, **config)