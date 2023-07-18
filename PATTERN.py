def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
    #trying bruteforce first
    mindifferencesofar =999999999
    ans=[]
    for i in range(len(forwardRouteList)):
        fwrdcurrent = forwardRouteList[i][1]
        for j in range(len(returnRouteList)):
            retcurrent = returnRouteList[j][1]
            curr = fwrdcurrent+retcurrent
            if curr <=maxTravelDist:
                if mindifferencesofar > (maxTravelDist-curr):
                    mindifferencesofar = maxTravelDist - curr
                    ans.append([forwardRouteList[i][0],returnRouteList[j][0]])
    return ans


print(routePairs(7000,[[1,2000],[2,4000],[3,6000]],[[1,2000]]))