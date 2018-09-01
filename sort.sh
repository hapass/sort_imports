git add .
git status -s | sed -e 's/\(.*\) -> \(.*\)/\1/g' | grep .*hx$ | cut -c4- | python sort.py