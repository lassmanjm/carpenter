import numpy as np
import pandas as pd
from IPython.display import Latex
# class GeneralArray:

class Table:
    def __init__(self,A,columns=None,borders='all'):
        self.df=pd.DataFrame(A,columns=columns).copy()
        self.df_bak=self.df.copy()
        self.borders=borders
        
    def rename(self,columns=[],newcolumns=[]):
        if not columns:
            try:
                if len(newcolumns)!=len(self.df.columns):
                    raise Exception('Incorrect number of column names')
                self.df.rename(columns={col:ncol for col,ncol in zip(self.df.columns,newcolumns)},inplace=True)
            except Exception as excpt:
                print('Error:',excpt.args)
        else:        
            if type(columns) is dict:
                self.df.rename(columns=columns,inplace=True)
            else:
                try:
                    if not newcolumns:
                        raise Exception('Must define new column names')
                    if len(columns)!=len(newcolumns):
                        raise Exception('Column rename lists are not equal length')
                    self.df.rename(columns={col:ncol for col,ncol in zip(columns,newcolumns)},inplace=True)
                except Exception as excpt:
                    print('Error:',excpt.args)

    def textrm(self,headers=[],columns=[]):
        if headers=='*':
            headers=self.df.columns
        if columns=='*':
            columns=self.df.columns
        Hdict={}
        for col in columns:
            self.df[col]=[r'\textrm{'+str(val)+'}' for val in self.df[col]]
        for head in headers:
            Hdict[head]=r'\textrm{'+str(head)+'}'
            self.df.rename(columns=Hdict,inplace=True)

    
    def Float2Str(self,columns,SF=4):
        if columns == '*' and '*' not in self.df.columns:
            # columns=self.df.columns[[item in [int,float] for item in self.df.dtypes]]
            columns=self.df.columns
        if type(SF)==list:
            try:
                if len(columns)!=len(SF):
                    raise Exception('SF does not match Columns')
                EL=['%%.%if'%sf for sf in SF]
                for el,col in zip(EL,columns):
                    self.df[col]=[el%val if type(val) in [int,float]  else val for val in self.df[col]]
            except Exception as excpt:
                print('Error:',excpt.args)
        else:
            el='%%.%if'%SF
            for col in columns:
                self.df[col]=[el%val if type(val) in [int,float]  else val for val in self.df[col]]
    def to_numpy(self):
        A=self.df.to_numpy().astype(str)
        cols=self.df.columns.to_list()
        return np.concatenate(([cols],A),0)        
    def Generate(self,Padding=''):
        vline='|'
        hline=r'\hline'
        hline1=r'\hline'
        vline1='' 
        if self.borders=='none':
            vline=''
            hline=''
            hline1=''
            vlin1=''
        elif self.borders=='columns':
            hline=''
            hline1=r'\hline \hline'
            vline1=r'|'
    
        A=self.to_numpy()
        numCols=A.shape[1]
        colList=['c']*numCols
        colList[0]+=vline1
        output=Padding+'\\begin{array}{|%s|}\n\\hline\n '%vline.join(colList)
        for i,line in enumerate(A):
            if i==0:
                H=hline1
            elif i==len(A)-1:
                H=r'\hline'
            else:
                H=hline
            output+=' & '.join(line) + r'\\ '+H+' \n'
        output+='\\end{array}'+Padding
        return output
    
    def display(self, Inline=False):
        if Inline==True:
            padding='$'
        else:
            padding='$$'
        display(Latex(self.Generate(Padding=padding)))

class Array(Table):
    pass


# def Array(A):
#     numCols=len(A[0])
#     colList='c'*numCols
#     output='\\begin{array}{%s}\n '%colList
#     for line in A:
#         output+=' & '.join(line) + '\\\\ \n '
#     output+='\\end{array}'
#     return output