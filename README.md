pytest-circleci
===============

py.test CircleCI Plugin

When running tests under CircleCI you can run on multiple machines. Circle sets
environment variables to indicate which machine you are running on. This plugin
ensures tests are split across the machines by reading these variables.

Once installed py.test will look for CIRCLE_NODE_TOTAL and CIRCLE_NODE_INDEX
environment variables to partition tests with.
