import sys
import os
import zipfile
import datetime

def zipping_process(directory, year, prefix, isdelete):
    if os.path.exists(directory):
        catalog_list = os.listdir(directory) # list all from catalog
        files_for_zip = filter(lambda x: x.endswith(year[2:] + '.zip'), catalog_list) # list files for zipping
        if files_for_zip.count(prefix + year + '.zip') > 0: files_for_zip.remove(prefix + year + '.zip')

        if len(files_for_zip) > 0:
            name_zip_file = os.path.join(directory, prefix + year + '.zip')
            if not os.path.exists(name_zip_file) and not zipfile.is_zipfile(name_zip_file):
                try:
                    zip_file_obj = zipfile.ZipFile(name_zip_file,'w')
                    zip_file_obj.close()
                except Exception as create_zip_error:
                    print('Error in creating zip-file: ' + name_zip_file + ' (' + str(type(create_zip_error))[6:-1] + ')')
                    return 3  # Error in creating zip-file
            try:
                zip_file_obj = zipfile.ZipFile(name_zip_file,'a')
            except Exception as open_zip_error:
                print('Error in opening zip-file: ' + name_zip_file + ' (' + str(type(open_zip_error))[6:-1] + ')')
                return 4  # Error in opening zip-file
            script_path = os.getcwd()
            os.chdir(directory)
            for i in files_for_zip:
                if not i in zip_file_obj.namelist():
                    try:
                        zip_file_obj.write(i)
                    except Exception as zip_exception_error:
                        print('Error in archiving: ' + i + ' (' + str(type(zip_exception_error))[6:-1] + ')')
                    else:
                        try:
                            if isdelete: os.remove(i)
                        except Exception as zip_exception_error:
                            print('Error in deleting (file archived): ' + i + ' (' + str(type(zip_exception_error))[6:-1] + ')')
            zip_file_obj.close()
            os.chdir(script_path)
            return 0
        else:
            return 2 # Files for archiving are absent
    else:
        return 1 # Catalog is absent

def folder_scanning(directory):
    result = []
    try:
        list = os.listdir(directory)
        for i in list:
            if os.path.isdir(os.path.join(directory, i)):
                result.append(i)
        return result
    except OSError:
        print('Folders "' + directory + '" not found. Check configuration file, please.')
        # mainmenu()
        exit()

def archiving_process(ini_file,report_type,year,isdelete=False,islog=False):
    if report_type == 'det_rep':
        print('Archiving of AU and AV files')
        directory = parse_ini_file(ini_file).get('path_det_reports')
        subdir = 'ATM'
    elif report_type == 'ejrn':
        print('Archiving of EJournal files')
        directory = parse_ini_file(ini_file).get('path_ejrn_reports')
        subdir = 'JOURNAL'
    elif report_type == 'receipt':
        print('Archiving of Receipts files')
        directory = parse_ini_file(ini_file).get('path_receipt_reports')
        subdir = 'Recept'
    else:
        print('Unknown report type!')
        return 1  # Unknown report type

    objects_in_folder = folder_scanning(directory)
    if len(objects_in_folder) > 0:
        print('Started: ' + str(datetime.datetime.now()))
        for i in objects_in_folder:
            if os.path.exists(os.path.join(directory,i,subdir)):
                print('../' + i + '/' + subdir + '/')
                result_zipping = zipping_process(os.path.join(directory,i,subdir),year,subdir,isdelete)
                if result_zipping == 0:
                    print('  + Ok')
                elif result_zipping == 1:
                    print('  - Error in path to directory')
                elif result_zipping == 3:
                    print('  - Error in creating zip-file')
                elif result_zipping == 4:
                    print('  - Error in opening zip-file')
                else:
                    print('  - Folder have not files for archiving.')
            else:
                print('../' + i + '/' + subdir + '/' + ' - Folder not found')
        print('Finished: ' + str(datetime.datetime.now()))
        print('Task finished successful!')
        return 0  # Archiving is successful
    else:
        print('Folders for archiving not found. Check path to a reports folder, please.')
        return 2 # No folder for archiving.

def parse_ini_file(ini_file):
    result = {}
    if os.path.exists(ini_file):
        file_obj = open(ini_file)
        for line in file_obj.readlines():
            if line[len(line)-1] == '\n':
                line = line[:-1]
            if 'path_det_reports=' in line:
                result['path_det_reports'] = line.split('=')[1][:-1]
            elif 'path_ejrn_reports=' in line:
                result['path_ejrn_reports'] = line.split('=')[1][:-1]
            elif 'path_rec_reports=' in line:
                result['path_receipt_reports'] = line.split('=')[1][:-1]
        file_obj.close()
    else:
        print('Configuration file not found.')
    return result

def year_entering():
    year = text_input('Enter year: ')
    try:
        year = int(year)
        if year >= 2010 and year <= 2050:
            year = str(year)
            return year
    except ValueError:
        None
    print('Entered wrong year.')
    # mainmenu()
    exit()

def text_input(msg):      # function used for interactive data input
  try:
    return raw_input(msg)  # this one is for python 2
  except NameError:
    return input(msg)      # this one is for python 3

def display_help():
    print("""
Script for archiving ATM reports.
Autor Eugen Shkil

Parameters from command line:
 -det_rep       Archiving files of detaled reports (au/av-files)
 -ejrn          Archiving files of electronic journals
 -receipt       Archiving files of electronic receipts
 -log           Log-file enabled
 -help or /?    This help


""")

#===========================================
if __name__ == '__main__':
    ini_file = os.path.join(os.getcwd(),'test_zipfile.ini')
    isdelete = False
    islog = False

    if len(sys.argv) == 1:
        archiving_process(ini_file,'det_rep',year_entering(),isdelete)
        archiving_process(ini_file,'ejrn',year_entering(),isdelete)
        archiving_process(ini_file,'receipt',year_entering(),isdelete)
    else:
        for arg in sys.argv[1:]:
            if arg in ['-det_rep', '-ejrn', '-receipt','/det_rep', '/ejrn', '/receipt', '-v', '/v']:
                archiving_process(ini_file,arg[1:],year_entering(),isdelete,islog)
            elif arg == '-help' or arg == '/?':
                display_help()
            else:
                print('\nError in parameters.')
    exit(0)