from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton, Factory
from fastapi import FastAPI

from domain.transformer_factory import TransformerFactory
from model.transformer import Transformer


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=[".endpoints"])

    app = Singleton(FastAPI)
    transformer_factory: Factory[Transformer] = Factory(TransformerFactory)
