def classifyPerson():
  resultList = ['not like','so so','very like']
  gamePercent = float(raw_input("gaming time percent:"))
  flyMiles = float(raw_input("flying miles per year:"))
  bookNum = float(raw_input("reading books per month:"))
  datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
  normMat, ranges, minVals = autoNorm(datingDataMat)
  inArray = array([flyMiles, gamePercent, bookNum])
  classifyResult = classify0((inArray - minVals)/ranges, normMat, datingLabels, 3)
  print "prediction result is: ", resultList[classifyResult - 1]