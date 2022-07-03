import codecs

def drop_files(directory, lib, problems):
    lib_file = codecs.open(directory + "\\library.xml", "w+", "UTF-8")
    lib_file.write(lib)
    lib_file.close()
    q_i = 1
    for problem in problems:
        problem_file = codecs.open(directory + "\\q" + str(q_i) + ".xml", "w+", "UTF-8")
        problem_file.write(problem)
        problem_file.close()
        q_i += 1

