#!/usr/bin/env python

######################################################.
# 		        Testing with pytest: 	             #
#                   QDESCP module                    #
######################################################.

import os
import pytest
from aqme.qdescp import qdescp
from aqme.xtb_to_json import read_json
import glob
import shutil

# saves the working directory
w_dir_main = os.getcwd()
qdescp_input_dir = w_dir_main + "/tests/qdescp_inputs"
if not os.path.exists(qdescp_input_dir):
    os.mkdir(qdescp_input_dir)
#
# # tests for parameters of csearch random initialzation
# @pytest.mark.parametrize(
#     "file, name, temp, acc, charge, mult, output_file, num, boltz, program",
#     [
#         # tests for conformer generation with RDKit
#         (
#             "pentane.xyz",
#             "pentane",
#             "300",
#             "0.2",
#             0,
#             1,
#             "pentane_conf_1.json",
#             1,
#             False,
#             "xtb",
#         ),
#         (
#             "pentane_rdkit.sdf",
#             "pentane_rdkit",
#             "273",
#             0.1,
#             -1,
#             1,
#             "pentane_rdkit_conf_1.json",
#             4,
#             True,
#             "xtb",
#         ),
#     ],
# )
# def test_qdescp_inputs(
#     file, name, temp, acc, charge, mult, output_file, num, boltz, program
# ):
#     os.chdir(qdescp_input_dir)
#     # runs the program with the different tests
#
#     qdescp(
#         w_dir_main=qdescp_input_dir,
#         files=file,
#         qdescp_temp=temp,
#         qdescp_acc=acc,
#         charge=charge,
#         mult=mult,
#         boltz=boltz,
#         program=program,
#     )
#
#     # tests here
#     numfiles = len(glob.glob(f"QDESCP/{name}_conf_*.json"))
#     assert numfiles == num
#
#     if boltz:
#         bfile = str(f"QDESCP/boltz/{name}_boltz.json")
#         assert os.path.isfile(bfile)
#
#     file = str("QDESCP/" + output_file)
#     json_data = read_json(file)
#     check_temp = json_data["program call"].split("--etemp ")[1].split(" ")[0]
#     check_acc = json_data["program call"].split("--acc ")[1].split(" ")[0]
#     check_charge = json_data["program call"].split("--chrg ")[1].split(" ")[0]
#     check_mult = json_data["program call"].split("--uhf ")[1].split(" ")[0]
#     assert check_temp == str(temp)
#     assert check_acc == str(acc)
#     assert check_charge == str(charge)
#     assert check_mult == str(mult - 1)
#
#
# # tests for parameters of csearch random initialzation
# @pytest.mark.parametrize(
#     "file, name, program, boltz",
#     [
#         # tests for conformer generation with RDKit
#         ("MeOH_NMR_conf_1.json", "MeOH_NMR", "nmr", True),
#     ],
# )
# def test_program(file, name, program, boltz):
#     os.chdir(qdescp_input_dir)
#     # runs the program with the different tests
#     qdescp(
#         w_dir_main=qdescp_input_dir,
#         files=file,
#         program=program,
#         boltz=boltz,
#     )
#     # tests here
#     if boltz:
#         bfile = str(f"QDESCP/boltz/{name}_boltz.json")
#         assert os.path.isfile(bfile)
#
#
# # tests for removing foler
# @pytest.mark.parametrize(
#     "remove, folder, file",
#     [
#         # tests for conformer generation with RDKit
#         (True, "tests/qdescp_inputs/QDESCP", "tests/qdescp_inputs/QDESCP_*"),
#     ],
# )
# def test_remove(remove, folder, file):
#     # os.chdir(w_dir_main)
#     shutil.rmtree(w_dir_main + "/" + folder)
#     for f in glob.glob(file):
#         os.remove(f)
