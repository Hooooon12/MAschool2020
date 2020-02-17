################################################################################
#  
#  Copyright (C) 2012-2013 Eric Conte, Benjamin Fuks
#  The MadAnalysis development team, email: <ma5team@iphc.cnrs.fr>
#  
#  This file is part of MadAnalysis 5.
#  Official website: <https://launchpad.net/madanalysis5>
#  
#  MadAnalysis 5 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  MadAnalysis 5 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with MadAnalysis 5. If not, see <http://www.gnu.org/licenses/>
#  
################################################################################


import logging
import shutil
import os
import commands
import glob
import logging

class DelphesMigration():

    def __init__(self):
        pass

    def Migrate(self):
        self.ChangeTreeNames()
        self.ApplyPatch()

    def ApplyPatch(self):
        installdir=os.getcwd()
        filename_input  = installdir+'/doc/genMakefile.bak'
        filename_output = installdir+'/doc/genMakefile.tcl'

        try:
           os.rename(filename_output,filename_input)
        except:
            logging.error('impossible to rename the file '+filename_output)
            return False

        try:
            input = open(filename_input)
        except:
            logging.error('impossible to open the file '+filename_input)
            return False
        try:
            output = open(filename_output,'w')
        except:
            logging.error('impossible to open the file '+filename_output+'MA5')
            return False
        for line in input:
            line=line.replace('libDelphes.','libDelphesMA5tune.')
            output.write(line)
        input.close()
        output.close()


    def ChangeTreeNames(self):
        installdir=os.getcwd()
        myfiles = glob.glob(installdir+'/readers/Delphes*.cpp')
        for myfile in myfiles:
            self.ChangeTreeName(myfile)


    def ChangeTreeName(self,filename):

        try:
            input = open(filename)
        except:
            return False

        try:
            output = open(filename+"~","w")
        except:
            return False

        for line in input:
            if line.find("treeWriter")!=-1 and line.find("ExRootTreeWriter")!=1:
                line = line.replace('"Delphes"','"DelphesMA5tune"')
            output.write(line)

        output.close()
        input.close()
        os.system("mv "+filename+"~ "+filename)
        return True

prog = DelphesMigration()
prog.Migrate()
