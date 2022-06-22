import mini_angr

if __name__ == '__main__':
    proj = mini_angr.Project('binaries/BIGbadEASYvm')
    print(proj.loader.main_object)
