# The following variables can be set from the command line or,
# for the first two, from the environment.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build

.PHONY: help Makefile clean latexpdf git-hours all

# The 'all' target performs a full cleanup, runs doctests, and
# builds a LaTeX PDF if the doctests pass.
# It is placed first so that running "make" without arguments
# defaults to displaying the help information.
all: clean
	@echo "Running doctests..."
	@$(SPHINXBUILD) -M doctest "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@if [ $$? -eq 0 ]; then \
		echo "Doctests passed. Building JSON and HTML output..."; \
		$(SPHINXBUILD) -M json "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O); \
		$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O); \
	else \
		echo "Doctests failed. Skipping JSON and HTML builds."; \
	fi

# Target to build JSON output using Sphinx
json:
	@$(SPHINXBUILD) -M json "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Target to clean all build artifacts
clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Clean everything listed in .gitignore
clean-gitignore:
	@echo "Cleaning all artifacts defined in .gitignore..."
	# Remove all __pycache__ directories recursively
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	# Remove all .pyc files recursively
	@find . -type f -name "*.pyc" -delete
	# Remove specific ignored top-level directories
	@rm -rf build/ .pytest_cache/

# The 'help' target provides a summary of available commands.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Target to build the LaTeX PDF using Sphinx
latexpdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Target to display estimated hours worked based on Git commit history.
# Uses the 'git-hours' tool (https://pypi.org/project/git-hours/).
# NOTE: No command-line arguments are supported—runs with default settings.
git-hours:
	@git-hours

# Run GitStats
git-stats:
	@echo "Generating GitStats report ..."
	@mkdir -p $(BUILDDIR)/gitstats
	@gitstats . $(BUILDDIR)/gitstats
	@echo "Report saved to $(BUILDDIR)/gitstats/index.html"

# Catch-all target: routes any unknown target to Sphinx using
# the "make mode" option. $(O) is a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
