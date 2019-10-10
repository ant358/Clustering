import tabula
import pandas as pd

# note need to use an r to convert the paths to raw or change the \ for /'s
#df0 = pd.read_csv('C:\Users\AGW_W540\Google Drive\Python\Glen_R_for_A\Results_df.csv')
#print(df0.head())

# see https://github.com/chezou/tabula-py
#check setup is ok
#tabula.environment_info()

# Read pdf into DataFrame
#df = tabula.read_pdf(r"C:\Users\AGW_W540\Google Drive\Python\Glen_R_for_A\S10np95[99].pdf", pages='all')
#print(df.head())

# Read remote pdf into DataFrame
#df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
#print(df2.head())
convert PDF into CSV
tabula.convert_into(r"C:\Users\AGW_W540\Google Drive\Python\Glen_R_for_A\S10np95[99].pdf", 
r"C:\Users\AGW_W540\Google Drive\Python\Glen_R_for_A\S10np95[99].csv", output_format="csv", pages='all')

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all)