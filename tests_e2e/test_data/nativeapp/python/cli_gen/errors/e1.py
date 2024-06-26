# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from snowflake.snowpark.functions import udf


# Should be rejected by Snowpark since type hints are absent, sql should not be in the final output.
@udf(name="echo_fn_2")
def echo_fn_2(echo) -> str:
    return "echo_fn: " + echo


"""
Warning message generated by the CLI on skipping this file:
Could not fetch Snowpark objects from /Users/bgoel/snowcli/tests_e2e/test_data/nativeapp/python/cli_gen/errors/e1.py due to the following Snowpark-internal error:
 An exception occurred while executing file:  the number of arguments (1) is different from the number of argument type hints (0)
"""
