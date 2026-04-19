#!/usr/bin/env bash
# setup.sh — Install all dependencies for hwp-pipeline
#
# Prerequisites: Java 11+, Maven, Python 3.10+, Node.js 18+ (optional, for HWP reading)
#
# Usage:
#   bash setup.sh          # Install everything
#   bash setup.sh --java   # Java converter only
#   bash setup.sh --python # Python HWPX tools only
#   bash setup.sh --node   # Node.js HWP reader only

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
JAVA_DIR="$SCRIPT_DIR/java"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERR]${NC} $*" >&2; }

install_java() {
    info "Setting up HWP-to-HWPX converter (Java)..."

    if ! command -v java &>/dev/null; then
        error "Java not found. Install Java 11+ first."
        error "  macOS: brew install openjdk@11"
        error "  Ubuntu: sudo apt install openjdk-11-jdk"
        return 1
    fi

    if ! command -v mvn &>/dev/null; then
        error "Maven not found. Install Maven first."
        error "  macOS: brew install maven"
        error "  Ubuntu: sudo apt install maven"
        return 1
    fi

    # Check if fat JAR already exists
    if [[ -f "$JAVA_DIR/hwp2hwpx-fat.jar" ]]; then
        info "Fat JAR already exists: $JAVA_DIR/hwp2hwpx-fat.jar"
        return 0
    fi

    # Clone hwp2hwpx if source not present
    local BUILD_DIR
    BUILD_DIR="$(mktemp -d)"
    info "Cloning hwp2hwpx into $BUILD_DIR..."
    git clone --depth 1 https://github.com/neolord0/hwp2hwpx.git "$BUILD_DIR/hwp2hwpx"

    # Copy our pom.xml (with shade plugin and Java 11 target) over the original
    cp "$JAVA_DIR/pom.xml" "$BUILD_DIR/hwp2hwpx/pom.xml"

    # Copy Convert.java to the build directory
    cp "$JAVA_DIR/Convert.java" "$BUILD_DIR/hwp2hwpx/"

    # Build
    info "Building fat JAR..."
    cd "$BUILD_DIR/hwp2hwpx"
    mvn package -DskipTests -q

    # Copy fat JAR back
    cp "$BUILD_DIR/hwp2hwpx/target/hwp2hwpx-fat.jar" "$JAVA_DIR/hwp2hwpx-fat.jar"
    info "Fat JAR built: $JAVA_DIR/hwp2hwpx-fat.jar"

    # Cleanup
    rm -rf "$BUILD_DIR"
    cd "$SCRIPT_DIR"

    info "Java setup complete."
}

install_python() {
    info "Setting up HWPX editing tools (Python)..."

    if ! command -v python3 &>/dev/null; then
        error "Python 3 not found."
        return 1
    fi

    python3 -m pip install -U python-hwpx lxml 2>/dev/null || \
    pip install -U python-hwpx lxml

    info "Python setup complete."
}

install_node() {
    info "Setting up HWP reader (Node.js)..."

    if ! command -v node &>/dev/null; then
        warn "Node.js not found. Skipping HWP reader setup."
        warn "Install Node.js 18+ if you need HWP-to-JSON/Markdown conversion."
        return 0
    fi

    npm install -g @ohah/hwpjs 2>/dev/null || {
        warn "npm global install failed. Try: sudo npm install -g @ohah/hwpjs"
    }

    info "Node.js setup complete."
}

# Parse arguments
if [[ $# -eq 0 ]]; then
    install_java
    install_python
    install_node
    echo ""
    info "All done! See README.md for usage examples."
else
    case "$1" in
        --java)   install_java ;;
        --python) install_python ;;
        --node)   install_node ;;
        *)
            echo "Usage: bash setup.sh [--java|--python|--node]"
            exit 1
            ;;
    esac
fi
