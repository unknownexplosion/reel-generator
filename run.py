#!/usr/bin/env python3

import os
os.environ['PORT'] = '8002'

from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8002)