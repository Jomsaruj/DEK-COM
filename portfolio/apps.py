from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """Generate the portdolio"""

    name = 'portfolio'

    def ready(self):
        """prepare for the portfolio."""
        import portfolio.signals

