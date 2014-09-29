
import os


class CircleCIError(Exception):
    """Raised for problems running the CirleCI py.test plugin"""


def read_circleci_env_variables():
    """Read and convert CIRCLE_* environment variables"""
    circle_node_total = int(os.environ.get("CIRCLE_NODE_TOTAL", "1").strip())
    circle_node_index = int(os.environ.get("CIRCLE_NODE_INDEX", "0").strip())

    if circle_node_index >= circle_node_total:
        raise CircleCIError("CIRCLE_NODE_INDEX={} >= CIRCLE_NODE_TOTAL={}, should be less".format(circle_node_index, circle_node_total))

    return (circle_node_total, circle_node_index)


def pytest_report_header(config):
    """Add CircleCI information to report"""
    circle_node_total, circle_node_index = read_circleci_env_variables()
    return "CircleCI total nodes: {}, this node index: {}".format(circle_node_total, circle_node_index)


def pytest_collection_modifyitems(session, config, items):
    """
    Use CircleCI env vars to determine which tests to run

    - CIRCLE_NODE_TOTAL indicates total number of nodes tests are running on
    - CIRCLE_NODE_INDEX indicates which node this is

    Will run a subset of tests based on the node index.

    """
    circle_node_total, circle_node_index = read_circleci_env_variables()

    items.sort()
    for index, item in enumerate(list(items)):
        if (index % circle_node_total) != circle_node_index:
            items.remove(item)
