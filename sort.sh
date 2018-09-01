git add .
git status -s | sed -e 's/\(.*\) -> \(.*\)/R  \2/g' | grep .*hx$ | cut -c4- | python sort.py