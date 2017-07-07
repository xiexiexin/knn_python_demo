#函数名：autoNorm
#输入：dataSet为原始数据二维数组
#输出：normDataSet归一化之后的二维数组，ranges为每一列最大值减去最小值的范围，minVals为每一列的最小值。
def autoNorm(dataSet):
  minVals = dataSet.min(0)
  maxVals = dataSet.max(0)
  ranges = maxVals - minVals
  normDataSet = zeros(shape(dataSet))
  m = dataSet.shape[0]
  normDataSet = dataSet - tile(minVals, (m,1))
  normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
  return normDataSet, ranges, minVals