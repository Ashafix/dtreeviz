from sklearn import tree
from sklearn.datasets import load_boston, load_iris
import dtreeviz.trees

regr = tree.DecisionTreeRegressor(max_depth=2)
boston = load_boston()
regr.fit(boston.data, boston.target)

classifier = tree.DecisionTreeClassifier(max_depth=2)  # limit depth of tree
iris = load_iris()
classifier.fit(iris.data, iris.target)


def change_classifier(colors):
    viz = dtreeviz.trees.dtreeviz(classifier,
                                  iris.data,
                                  iris.target,
                                  target_name='variety',
                                  feature_names=iris.feature_names,
                                  class_names=["setosa", "versicolor", "virginica"],  # need class_names for classifier
                                  colors=colors
                                  )

    viz.view()


def change_regression(colors):
    viz = dtreeviz.trees.dtreeviz(regr,
                                  boston.data,
                                  boston.target,
                                  target_name='price',
                                  feature_names=boston.feature_names,
                                  colors=colors)
    viz.view()


changes = {'no changes': None,
           'wedge': {'wedge': '#ff0000'},
           'split line': {'split_line': '#ff0000'},
           'markers': {'scatter_marker': '#ff0000'},
           'split_prev': {'scatter_marker': '#ff0000'},
           'axis_label': {'axis_label': '#ff0000'},
           'title': {'title': '#ff0000'},
           'x/y/z-labels': {'xlabel': '#ff0000', 'ylabel': '#00ff00', 'zlabel': '#0000ff'},
           'classes': {'classes':  [
                        None, # 0 classes
                        None, # 1 class
                       ["#FEFEBB","#a1dab4"], # 2 classes
                       ["#ff0000","#00ff00",'#0000ff'], # colors were changed here
                       ["#FEFEBB","#D9E6F5",'#a1dab4','#fee090'], # 4
                       ["#FEFEBB","#D9E6F5",'#a1dab4','#41b6c4','#fee090'], # 5
                       ["#FEFEBB",'#c7e9b4','#41b6c4','#2c7fb8','#fee090','#f46d43'], # 6
                       ["#FEFEBB",'#c7e9b4','#7fcdbb','#41b6c4','#225ea8','#fdae61','#f46d43'], # 7
                       ["#FEFEBB",'#edf8b1','#c7e9b4','#7fcdbb','#1d91c0','#225ea8','#fdae61','#f46d43'], # 8
                       ["#FEFEBB",'#c7e9b4','#41b6c4','#74add1','#4575b4','#313695','#fee090','#fdae61','#f46d43'], # 9
                       ["#FEFEBB",'#c7e9b4','#41b6c4','#74add1','#4575b4','#313695','#fee090','#fdae61','#f46d43','#d73027'] # 10
                   ]},
           'rect_edge': {'rect_edge': '#ff0000'},
           'text': {'text': '#ff0000'},
           'highlight': {'highlight': '#ff0000'},
           'text_wedge': {'text_wedge': '#ff0000'},
           'default': {'default': '#ff0000'},
           'major tick': {'tick_major': '#ff0000'},
           'node_label': {'node_label': '#ff0000'},
           'leaf_label': {'leaf_label': '#ff0000'},
           'legend_edge': {'legend_edge': '#ff0000'}
           }

regression_changes = ['no changes', 'wedge', 'split line', 'markers', 'axis_label']
classifier_changes = ['no changes', 'wedge', 'text_wedge', 'classes', 'x/y/z-labels', 'title', 'text', ]

# missing elements
# 'legend_edge', 'highlight'

for f, relevant_changes in zip((change_regression, change_classifier),
                               (regression_changes, classifier_changes)):
    for change in relevant_changes:
        f(changes[change])
        input(f'{change}: press any key for next image')


