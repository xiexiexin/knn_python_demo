#函数名：datingClassTest
#输入：无
#输出：无，但是会打印出错个数及错误率。
def datingClassTest():
  hoRatio = 0.50      #hold out 10%
  datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
  normMat, ranges, minVals = autoNorm(datingDataMat)
  m = normMat.shape[0]
  numTestVecs = int(m*hoRatio)
  errorCount = 0.0
  for i in range(numTestVecs):
      classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
      print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
      if (classifierResult != datingLabels[i]): errorCount += 1.0
  print ("the total error rate is: %f" % (errorCount/float(numTestVecs)))
  print (errorCount)