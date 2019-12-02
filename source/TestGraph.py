from graphviz import Digraph

dot = Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bede the Wise')
dot.node('L', 'Sir Anton the Brave')

dot.edges(['AB', 'AL'])

new_dot = Digraph()
new_dot.node('c', "new1")
new_dot.node('d', "new2")
new_dot.node('e', "new3")

new_dot.edges(['cd', 'ce'])

dot.subgraph(new_dot)
dot.edge('A','c')

print(dot.source)

dot.render('test-output/round-table.gv', view=True)
