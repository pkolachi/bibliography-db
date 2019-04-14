#!/usr/bin/env python3

import io  ;
import os  ; 
import sys ;

try :
  import bibtexparser as bibp ; 
except ImportError :
  print("Required module bibtexparser is uninstalled.\nRun pip install bibtexparser", file=sys.stderr) ; 
  sys.exit(1) ; 

def main() : 

  # output prefix
  outpref = sys.argv[3] ; 

  # if there are any new files in the <arxiv-folder> missing from bibfiles 
  # list them
  if arvix_folder : 
    paperids = [os.path.splitext(fnm)[0] for fnm in os.listdir(arxiv_folder)] ; 
    # strip version suffixes from paperids (e.g. 1904.04063v2)
    mpaperids = [pid for pid in paperids if pid not in bibdb] ; 
    print("Arxiv paperids missing from all bib databases\t{0}".format(' '.join(mpaperids))) ; 
    
  return 0 ; 

if __name__ == '__main__' :
  main() ; 
