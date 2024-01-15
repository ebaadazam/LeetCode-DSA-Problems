'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the
simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple
consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as
file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
'''


def simplify_path(path):
    stack = []  # we will append only the names of files or directories in the stack
    current  = ""  # keeps track of the recent file or directory name

    for i in path:
        if i == "/":  # if we reach a "/" then we are either appending or popping a file

            # here we are popping a file if we encounter ".."
            if current == "..":
                if stack:
                    stack.pop()

            # here we are appending a file if current is not null and current is not equals to "."
            elif current != "" and current != ".":
                stack.append(current)

            # after appending the value of current, we are again setting it to empty because our main moptive of creating this "current" varialble
            # just to append the recent word into the stack
            current = ""
        else:
            current = current + i
    return "/" + "/".join(stack)

path = "/../abc//def/./"
path2 = "/abc//..//def/pkl/"
path3 = "/a//b////c/d//././/.."
print(simplify_path(path))
print(simplify_path(path2))
print(simplify_path(path3))