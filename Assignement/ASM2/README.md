# Assignment 2 - Trees

## Your Task

Maintain a **tree** where each node in the tree holds an **integer** value as its key, as well as the property **subtree_value**.
The value of **subtree_value** is equivalent to the **maximum** number in the subtree of its children rooted at this node.

For example:

```
  A(5)
   / \
 C(2) D(8)
  |
 B(10)
```

Where `A = 5`, `C = 2`, `D=8`, `B=10` -- then Node A would have `subtree_value`
value `10`. `C` and `B` would also have `10`, but D would have `8`.

## Code

### `node.py`

This file holds all information about the node in the tree.

#### Properties

| Name              |   Type  | Description                                         |
|:------------------|:-------:|:----------------------------------------------------|
| **children**      |  `list` | Holds all children to this node as pointers.        |
| **parent**        | `*Node` | Holds the pointer to the parent.                    |
| **key**           |  `int`  | Holds the key                                       |
| **subtree_value** |  `int`  | The maximum key of the subtree rooted at this node. |


#### Functions

```
node.add_child(child_node)
```

* Adds the child to the node.
* Runs calculations for subtree value.

```
node.is_external()
```
* Checks if the node is a leaf.

```
node.get_children()
```
* Returns the list of children.


### `tree.py`

The main tree file, holds all interaction with trees and nodes.

#### Properties

| Name     |   Type  | Description           |
|:---------|:-------:|:----------------------|
| **root** | `*Node` | Root node of the tree |

#### Functions

```
put(node, child)
```

* Add the child to the node.

```
flatten(node)
```

* Flatten the subtree of the node.
* Perform calculations


```
swap(subtree_a, subtree_b)
```

* Swap subtree A with subtree B.


## Testing

We have provided you with some test cases in the `tests` directory of this
repository. We will be using unit tests provided with the `unittest` package
of python.

**Running Tests**

From the base directory (the one with `node.py` and `tree.py`), run

```
python -m unittest -v tests/test_simple_functions.py
```


## Working with git

We will be using git to manage the code versioning and submit your work.

If you haven't done much with git, then head over to some of these:

* https://www.atlassian.com/git/tutorials
* https://learngitbranching.js.org/
* https://git-scm.com/docs/gittutorial
* https://try.github.io/

### Workflow.

**Setup**

* Get the code from the repo to your machine:

```
git clone <url_here>
```

**Working**

* Do some _things_.

* (Optional) Add the changes of your work by doing either:
  * ``git add node.py tree.py``  --> this adds all changes to both files.
  * ``git add -p`` --> steps through changes that you made.
* Commit the changes, with either:
  * ``git commit <file_name_here> -m "your commit message here"`` --> commit all changes
  * ``git commit -p -m "your commit message here"`` --> step through changes and commit.
* Push your submission, either:
  * ``git push``
  * ``git push origin master``


When you have successfully pushed your changes, your code will be marked and you will get feedback.
You can also check your submissions on Ed.
