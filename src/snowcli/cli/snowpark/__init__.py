import typer

from snowcli.cli.snowpark.function import app as function_app
from snowcli.cli.snowpark.package import app as package_app
from snowcli.cli.snowpark.procedure import app as procedure_app
from snowcli.cli.common.flags import DEFAULT_CONTEXT_SETTINGS

app = typer.Typer(name="snowpark", context_settings=DEFAULT_CONTEXT_SETTINGS)

app.add_typer(function_app)
app.add_typer(package_app)
app.add_typer(procedure_app)
