import os
import shutil
from multiprocessing.dummy import Pool
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description=
                                 'Intechgambit software')
parser.add_argument('-db', '--database', type=str,
                    dest='database',
                    help='select database path')
parser.add_argument('-l', '--label', type=str,
                    dest='label',
                    help='choose results directory label')

args = parser.parse_args()


class BLAST:
    def __init__(self):
        self.blast_file_dir = f'{os.path.expanduser("~")}/stDatApp/temp/raw_files'
        logfile = f"{os.path.expanduser('~')}/stDatApp/appLogs"
        date_str = str(datetime.today().date())
        self.runtime = os.path.join(logfile, f"{date_str}-runtime.log")
        self.error = os.path.join(logfile, f"{date_str}-runtime_errors.log")
        self.summary = os.path.join(logfile, f"{date_str}-run_summary.log")

    def summary_logs(self):
        return open(self.summary, 'a')

    def error_logs(self):
        return open(self.error, 'a')

    def runtime_logs(self):
        return open(self.runtime, 'a')

    def database_search(self, input_search):
        """Launch multiple processes per core."""
        filename = os.path.basename(input_search)
        blast_path = f"{os.path.expanduser('~')}/stDatApp/ncbi-blast-2.13.0+/bin"
        out_dir = f"{os.path.expanduser('~')}/stDatApp/blast_results"
        label = str(args.label).replace(" ", "_").strip()
        out_dir = os.path.join(out_dir, label)
        os.makedirs(out_dir, exist_ok=True)
        blast_db = args.database
        out_str = str(filename).rsplit("/", 1)[0].rsplit("/", 1)[-1]
        file_path = os.path.join(out_dir, f"{out_str}.csv")
        blast_exec = f'{blast_path}/blastn -db {blast_db}' \
                     f' -query {input_search} -outfmt "6 delim=, sseqid sacc sallacc qacc qlen slen sscinames' \
                     f'  pident length qcovs mismatch gapopen gaps qstart qend sstart send evalue bitscore ' \
                     f'qframe sframe " ' \
                     f'-out {file_path}'
        os.system(blast_exec)
        self.runtime_logs().writelines(f"{datetime.today()} Blast completed processing {file_path} \n")
        return self.blast_file_dir

    def get_blast_files(self):
        blast_in = []
        for path, sub_dirs, files in os.walk(self.blast_file_dir):
            for file in files:
                full_path = os.path.join(path, file)
                blast_in.append(full_path)
                self.runtime_logs().writelines(f"{datetime.today()} Preparing file {full_path} for processing \n")
        return blast_in

    def cleaner(self):
        shutil.rmtree(self.blast_file_dir)


if __name__ == '__main__':
    pool = Pool(os.cpu_count())
    process = BLAST()
    process_input = BLAST().get_blast_files()
    pool.map(BLAST().database_search, process_input)
    pool.close()
    BLAST().summary_logs().writelines(f"{datetime.today()} BLAST has completed!! \n")
