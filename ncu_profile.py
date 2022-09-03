#!/usr/bin/env python3

import argparse
import subprocess as subp

from ncu_metrics import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bin", required=True, help="Binary executable.")
    args = parser.parse_args()

    cmd = "ncu --metrics "
    cmd += ",".join(list(METRICS_COMPUTE().keys())) + ","
    cmd += ",".join(list(METRICS_MEMORY().keys())) + ","
    cmd += ",".join(list(METRICS_ROOFLINE().keys())) + ","
    cmd += ",".join(list(METRICS_INSTRUCTION().keys())) + ","
    cmd += ",".join(list(METRICS_SCHEDULER().keys())) + ","
    cmd += ",".join(list(METRICS_OCCUPANCY().keys())) + ","
    cmd += ",".join(list(METRICS_BRANCH().keys()))

    bin_cmd = (args.bin).strip('"').strip("'")
    cmd += f" -f -o ncu-perf {bin_cmd}"

    subp.Popen(
        cmd.split(" "),
        stdin=subp.PIPE,
        stdout=subp.PIPE,
        stderr=subp.STDOUT,
    ).wait()


if __name__ == "__main__":
    main()
