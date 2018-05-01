#!/usr/bin/env bash
# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variables defined
# in the .travis.yml in the top level folder of the project.

# License: 3-clause BSD

set -e

python --version

run_tests() {
    pytest -v --durations=0
}

if [[ "$RUN_TESTS" == "true" ]]; then
    run_tests
fi
