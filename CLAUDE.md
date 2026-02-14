# Claude AI Collaboration Guidelines

This document outlines the preferred workflow and priorities for AI-assisted development on this project.

## Session Goals & Approach

### Research-First Methodology
- **Web search for options**: When implementing features, research available solutions thoroughly before choosing
- **Comparative analysis**: Evaluate multiple options based on specific requirements
- **Documentation verification**: Cross-reference implementations against official documentation
- **Best practices**: Check for established patterns and community recommendations

### Implementation Priorities

1. **Preserve existing functionality**: Maintain current behavior unless explicitly changing it
2. **Compatibility first**: Ensure new features work with existing customizations
3. **Test locally**: Build and verify changes before committing
4. **Incremental changes**: Make focused, reviewable commits

## Code Attribution Standards

### Inline Comments
When AI contributes code, mark it with attribution comments:

**Single line changes (≤3 lines):**
```python
variable = "value"  # written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
```

**Multi-line changes (>3 lines):**
```python
# Start: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
def function():
    # code here
    pass
# End: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
```

### Git Commit Attribution
Always include co-author in commits:
```
Co-Authored-By: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
```

## Git Workflow Preferences

### Commit Messages
- Follow existing repository style (brief, lowercase, descriptive)
- Include context in commit body when helpful
- Always add AI co-author attribution

### Branch Strategy
- Use descriptive branch names (e.g., `llm/darkmode` for AI-assisted features)
- Keep branches focused on single features/changes

### Pull Requests
**PR Description Format:**
- Clear summary of changes
- Implementation details
- Testing information
- **Development process section** explaining how AI was used:
  1. Research phase
  2. Evaluation criteria
  3. Implementation approach
  4. Verification steps

## Code Review Process

### When Requesting Reviews
- Be specific about what to review
- Request sympathetic, encouraging feedback
- Focus on learning opportunities

### AI-Generated Reviews Should Include
- Positive feedback on what works well
- Critical issues (blocking problems)
- Suggestions for improvement
- Encouragement and constructive tone
- Explanation of how the review was generated

## Development Environment

### Local Setup
- Use virtual environments (`venv/`)
- Keep `requirements.txt` updated with all dependencies
- Test builds locally before pushing
- Run development servers to verify changes

### Dependencies
- Pin versions for critical dependencies
- Use version ranges for flexibility where appropriate
- Always update requirements.txt when adding packages

## Communication Style

### With Users
- Be concise and clear
- Avoid emoji unless explicitly requested
- Provide markdown links to files/lines for easy navigation
- Format as `[filename.ext:line](path/to/file#Lline)`

### Research & References
**Always include references when making factual claims**, especially for:
- Security vulnerabilities and statistics
- Best practices and industry standards
- Research findings and studies
- Library/framework capabilities and limitations
- Performance benchmarks

**Reference Format:**
- Use markdown hyperlinks: `[Source Name](URL)`
- Include a "Sources:" or "References:" section at the end of responses
- For web search results, cite authoritative sources (official docs, research papers, industry analysis)
- Prefer primary sources over secondary when available

**When to Include References:**
- Discussing security concerns or vulnerabilities
- Citing statistics or research data
- Recommending specific approaches based on industry standards
- Comparing technologies or tools
- Explaining complex technical concepts

### Documentation
- Explain AI usage transparently in PRs
- Provide context for reviewers
- Include reasoning behind implementation choices
- Cite sources for technical decisions when based on research

## Project-Specific Notes

### This Website
- Built with Sphinx
- Theme: Furo (with dark mode support)
- No sidebars on pages
- Custom CSS in `source/static/css/custom.css`
- FontAwesome icons via CDN
- Bibliography support via sphinxcontrib-bibtex

### Build Process
```bash
source venv/bin/activate
make html
# Serve locally for testing:
cd build/html && python3 -m http.server 8000
```

## Future Session Patterns

### For Similar Feature Additions
1. Research available options with web search
2. Evaluate based on requirements (features, compatibility, maintenance)
3. Implement with proper attribution
4. Test locally with build + dev server
5. Commit with descriptive message + co-author
6. Create PR with detailed description
7. Optional: Perform AI-assisted code review
8. Apply feedback while preserving project preferences

### For Code Reviews
1. Examine actual changes (git diff)
2. Read modified files in full
3. Research best practices for the technology
4. Provide balanced feedback (positives + improvements)
5. Be encouraging and educational
6. Include section on how AI was used
7. Post as PR comment with full context

## Key Learnings from Initial Session

- **Missing dependencies** are a common oversight - always verify requirements.txt
- **Attribution verbosity** is a preference decision - respect project norms
- **Fork vs clone** matters for GitHub PRs - proper forks enable cross-repo PRs
- **Local testing** catches issues before pushing
- **Web research** provides better solutions than guessing

---

*This document reflects the workflow established during the dark mode theme implementation session (2026-02-13)*
