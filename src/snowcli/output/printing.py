from __future__ import annotations

from datetime import datetime
from json import JSONEncoder
from typing import List, Optional, Dict

import click
from rich import box, print, print_json
from rich.table import Table
from snowflake.connector.cursor import SnowflakeCursor

from snowcli.output.formats import OutputFormat


class CustomJSONEncoder(JSONEncoder):
    """Custom JSON encoder handling serialization of non-standard types"""

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


def print_db_cursor(
    cursor: SnowflakeCursor,
    columns: Optional[List[str]] = None,
) -> None:
    """
    Prints results fetched by cursor using specified format.

    :param cursor: snowflake cursor for fetching results
    :param columns: list of columns that should be included in output, if
        not provided then all columns are returned
    :return:
    """
    context = click.get_current_context()
    output_format = OutputFormat(context.find_root().params.get("output_format"))

    result = cursor.fetchall()
    column_names = [t[0] for t in cursor.description]
    columns = columns or column_names

    data = [{k: v for k, v in zip(column_names, row) if k in columns} for row in result]

    if output_format == OutputFormat.TABLE:
        _print_table(column_names, data, columns)
    elif output_format == OutputFormat.JSON:
        import json

        print_json(json.dumps(data, cls=CustomJSONEncoder))
    else:
        raise Exception(f"Unknown {output_format} format option")


def _print_table(column_names: List[str], data: List[Dict], columns: List[str]):
    table = Table(show_header=True, box=box.ASCII)
    for column in column_names:
        if column in columns:
            table.add_column(column)
    for row in data:
        table.add_row(*[str(i) for i in row.values()])
    print(table)
