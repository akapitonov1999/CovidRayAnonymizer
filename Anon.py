def anon_dir(main_dir, new_dir):
    os.chdir(main_dir)
    lst_main_dir = os.listdir()
    iteration_main_dir = 0
    while iteration_main_dir != len(lst_main_dir):
        iteration_final_dir = 0
        os.chdir(lst_main_dir[iteration_main_dir])
        #print(os.getcwd())
        #print('New dir', os.listdir())
        lst_sub_dir = os.listdir()
        os.chdir(lst_sub_dir[0])
        #print('final dir', os.listdir())
        lst_final_dir = os.listdir()
        path = new_dir + '\\' + str(iteration_main_dir)
        os.mkdir(path, mode=777)
        while iteration_final_dir != len(lst_final_dir):
            dataset = pydicom.dcmread(lst_final_dir[iteration_final_dir])
            #print(dataset)
            dataset.PatientName = ''
            dataset.PatientID = ''
            dataset.PatientBirthDate = '00010101'
            dataset.StudyID = ''
            dataset.StudyDate = '00010101'
            dataset.SeriesDate = '00010101'
            dataset.ContentDate = '00010101'
            dataset.AcquisitionDateTime = '00010101'
            dataset.StudyTime = '000000.00'
            dataset.SeriesTime = '000000.00'
            dataset.AcquisitionTime = '000000.00'
            dataset.ContentTime = '000000.00'
            dataset.AccessionNumber = ''
            dataset.InstitutionName = ''
            dataset.ReferringPhysicianName = ''
            dataset.OperatorName = ''
            #print(path)
            dataset.save_as(path+ '\\' + str(iteration_final_dir) + '.dcm')
            iteration_final_dir += 1
        
        os.chdir(main_dir)
        iteration_main_dir += 1
        print('anonymization completed', iteration_main_dir)
