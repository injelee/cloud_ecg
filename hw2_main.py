from bme590hrmfixed.get_ecg3 import Ecg
from csvtojson import csvtojson
import glob


if __name__ == "__main__":
    """
    
    Main script that calls all methods of Ecg in order to 
    process data contained in an input csv file and output a .txt file
    containing all estimated heart rate parameters 
    
    """
    # Importing csv data
    # Create the list of file
    # list_of_files = glob.glob('test_data/*.csv')
    # for file_name in list_of_files:
    # data = open(file_name, 'r')
    data = csvtojson()

    ecg_data = Ecg(data, update_time=5,
                   brady_threshold=60, tachy_threshold=100, user_sec=10)
    ecg_data.prep_data()
    ecg_data.get_max_peak()
    ecg_data.get_inst_hr()
    ecg_data.get_avghr()
    ecg_data.get_output()
    ecg_data.as_dict()
