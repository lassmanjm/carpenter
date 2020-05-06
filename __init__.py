import numpy as np
import pandas as pd
from IPython.display import Latex
# class GeneralArray:

class Table:
    def __init__(self,A,columns=None,borders='all'):
        self.df=pd.DataFrame(A,columns=columns).copy()
        self.df_bak=self.df.copy()
        self.borders=borders

    def textrm(self,headers=[],columns=[]):
        if headers=='*':
            headers=self.df.columns
        if columns=='*':
            columns=self.df.columns
        Hdict={}
        for head in headers:
            Hdict[head]=r'\textrm{'+str(head)+'}'
            self.df.rename(columns=Hdict,inplace=True)

        for col in columns:
            self.df[col]=[r'\textrm{'+str(val)+'}' for val in self.df[col]]
    
    def Float2Str(self,columns,SF=4):
        '''Poop2 poopyt
        adsfa
        afd'''
        if type(SF)==list:
            try:
                if len(columns)!=len(SF):
                    raise Exception('SF does not match Columns')
                EL=['%%.%if'%sf for sf in SF]
                for el,col in zip(EL,columns):
                    self.df[col]=[el%val for val in self.df[col]]
            except Exception as excpt:
                print('Error:',excpt.args)
        else:
            el='%%.%if'%SF
            for col in columns:
                self.df[col]=[el%val for val in self.df[col]]
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
            # print(line)
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


# from IPython.display import Latex, Math
# import numpy as np
# import pandas as pd
# A=(np.random.rand(4,4))
# col1=np.array(['a b c d'.split(' ')]).T
# adf=pd.DataFrame(A,columns='b c d e'.split(' '))
# adf['col1']=col1
# tab=Table(adf)
# tab.Float2Str(['b','e'],[1,3])
# tab.textrm(columns=['b','e'])
# display(Math(tab.Generate()))

# def Table(A,borders='all',center=True):
#     vline='|'
#     hline=r'\hline'
#     hline1=r'\hline'
#     vline1='' 
#     startEnd='$$'   
#     if borders=='none':
#         vline=''
#         hline=''
#         hline1=''
#         vlin1=''
#     elif borders=='outer':
#         hline=''
#         hline1=r'\hline \hline'
#         vline1=r'|'
   
#     if not center:
#         startEnd=''


#     numCols=len(A[0])
#     colList=['c']*numCols
#     colList[0]+=vline1
#     output=startEnd+'\\begin{array}{|%s|}\n\\hline\n '%vline.join(colList)
#     for i,line in enumerate(A):
#         if i==0:
#             H=hline1
#         elif i==len(A)-1:
#             H=r'\hline'
#         else:
#             H=hline
#         output+=' & '.join(line) + r'\\ '+H+' \n'
#     output+='\\end{array}'+startEnd
#     return output

# def Array(A):
#     numCols=len(A[0])
#     colList='c'*numCols
#     output='\\begin{array}{%s}\n '%colList
#     for line in A:
#         output+=' & '.join(line) + '\\\\ \n '
#     output+='\\end{array}'
#     return output