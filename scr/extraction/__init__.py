import sys
import os

if os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
) not in sys.path:
    sys.path.append(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )
