#函数名：file2matrix
#输入：文件名
#输出：returnMat为txt文本数据的前三列构成的二维数组
#     classLabelVector为txt文本数据第四列的分类信息的一维矢量
def file2matrix(filename):
  fr = open(filename)
  numberOfLines = len(fr.readlines())         #get the number of lines in the file
  returnMat = zeros((numberOfLines,3))        #prepare matrix to return
  classLabelVector = []                       #prepare labels return   
  fr = open(filename)
  index = 0
  for line in fr.readlines():
      line = line.strip()
      listFromLine = line.split('\t')
      returnMat[index,:] = listFromLine[0:3]
      classLabelVector.append(int(listFromLine[-1]))
      index += 1
  return returnMat,classLabelVector