import os
import shutil
import glob

mt22 = "main/mt22/parser/MT22.g4"
ast_gen = "main/mt22/astgen/ASTGeneration.py"
ast_gen_suite = "test/ASTGenSuite.py"
gen_dir = "../target"

target_fol = "../submit"
# check if target folder exists
if not os.path.exists(target_fol):
    os.mkdir(target_fol)
    
# copy files
shutil.copy(mt22, target_fol)
shutil.copy(ast_gen, target_fol)
shutil.copy(ast_gen_suite, target_fol)

gen_files = glob.glob(gen_dir + "/*")
for gen_file in gen_files:
    shutil.copy(gen_file, target_fol)

