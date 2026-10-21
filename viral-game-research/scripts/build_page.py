"""Inline report/web/data.json into the page template -> report/web/viral-game-evidence.html."""
import os
R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "report", "web")
t = open(os.path.join(R, "template.html")).read()
open(os.path.join(R, "viral-game-evidence.html"), "w").write(t.replace("__DATA__", open(os.path.join(R, "data.json")).read()))
print("ok")
