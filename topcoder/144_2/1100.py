class PowerOutage:
	
	def estimateTimeOut(self, fromJunction, toJunction, ductLength):
		totalTime = sum(ductLength)
		
		graph = {}
		size = len(fromJunction)
		
		for i in range(0, size):
			start = fromJunction[i]
			end = toJunction[i]
			length = ductLength[i]
			
			if not start in graph:
				graph[start] = []
			graph[start].append((end, length))
		
		return totalTime * 2 - self.deepestPath(0, graph)
		
	def deepestPath(self, node, graph):
		if not node in graph:
			return 0
		return max([self.deepestPath(nextNode, graph) + length for nextNode, length in graph[node]])
