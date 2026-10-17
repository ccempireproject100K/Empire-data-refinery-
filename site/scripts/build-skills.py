from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
SKILL_DIR = PUBLIC / 'content' / 'skills'
SKILL_DIR.mkdir(parents=True, exist_ok=True)

skills = [
    {
        'slug': 'agent-fundamentals',
        'name': 'Agent Fundamentals',
        'level': 'Beginner',
        'category': 'Foundations',
        'summary': 'Plan, build, and evaluate an AI agent using tools, observations, actions, and clear task boundaries.',
        'uses': ['Use when designing a new agent workflow.', 'Use when deciding whether a task needs an agent, a deterministic script, or a simple prompt.', 'Use when documenting an agent so another system can reproduce it.'],
        'capabilities': ['Agent loop design', 'Tool selection', 'Task decomposition', 'Failure handling', 'Evaluation planning'],
        'workflow': ['Define the user goal and success criteria.', 'Separate deterministic work from judgment and tool use.', 'Describe the agent loop: plan, act, observe, verify, and report.', 'Set permissions and failure boundaries before connecting tools.', 'Test with representative examples and record uncertainty.'],
        'sources': [
            {'title': 'Hugging Face AI Agents Course', 'url': 'https://huggingface.co/learn/agents-course/en/unit0/introduction', 'license': 'Course access is free; retain the source link and review the source terms before redistributing excerpts.'},
            {'title': 'Microsoft AI Agents for Beginners', 'url': 'https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/', 'license': 'Public Microsoft Learn course material; use source links and applicable Microsoft terms.'},
            {'title': 'Microsoft course repository', 'url': 'https://github.com/microsoft/ai-agents-for-beginners', 'license': 'MIT repository; verify the LICENSE file for copied code or text.'},
        ],
        'archiveNote': 'This is a derived workflow summary. It does not reproduce the source course transcript or lessons.',
        'connectors': [],
    },
    {
        'slug': 'agentic-rag',
        'name': 'Agentic RAG',
        'level': 'Intermediate',
        'category': 'Knowledge retrieval',
        'summary': 'Retrieve, rank, cite, and synthesize external information before an agent answers.',
        'uses': ['Use for research assistants and evidence-aware answers.', 'Use when source freshness, provenance, and citation quality matter.', 'Use when a knowledge base or document archive must be searched before action.'],
        'capabilities': ['Query decomposition', 'Retrieval and reranking', 'Citation tracking', 'Source quality checks', 'Uncertainty reporting'],
        'workflow': ['Translate the request into searchable sub-questions.', 'Choose an approved source set and record retrieval timestamps.', 'Retrieve primary or authoritative material before secondary commentary.', 'Attach source URLs to claims and distinguish facts from interpretation.', 'Check for contradictions, stale documents, and missing evidence before responding.'],
        'sources': [
            {'title': 'Microsoft AI Agents for Beginners — Agentic RAG', 'url': 'https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/what-is-agentic-rag/', 'license': 'Microsoft Learn source; retain attribution and link.'},
            {'title': 'Hugging Face AI Agents Course', 'url': 'https://huggingface.co/learn/agents-course/en/unit0/introduction', 'license': 'Course access is free; use a derived summary rather than copying lesson text.'},
        ],
        'archiveNote': 'Derived from public course concepts and adapted as a compact 20/20 research workflow.',
        'connectors': ['web-search', 'document-store'],
    },
    {
        'slug': 'tool-use-and-mcp',
        'name': 'Tool Use and MCP',
        'level': 'Intermediate',
        'category': 'Agent infrastructure',
        'summary': 'Connect an AI application to tools, resources, data sources, and workflows through explicit interfaces.',
        'uses': ['Use when an agent must call APIs or local tools.', 'Use when designing a reusable tool server for multiple AI clients.', 'Use when documenting tool inputs, outputs, permissions, and failure modes.'],
        'capabilities': ['Tool schemas', 'Resource access', 'Prompt templates', 'MCP server planning', 'Permission boundaries'],
        'workflow': ['Define each tool with a narrow name, purpose, input schema, output schema, and error contract.', 'Separate read-only resources from mutating actions.', 'Require explicit confirmation for consequential actions.', 'Log tool calls without recording secret values.', 'Test malformed inputs, timeouts, partial results, and revoked credentials.'],
        'sources': [
            {'title': 'Model Context Protocol introduction', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'Open protocol documentation; check the source repository terms before copying text or code.'},
            {'title': 'Agent Skills open format', 'url': 'https://agentskills.io/home', 'license': 'Open skills format; retain source attribution and verify current specification terms.'},
        ],
        'archiveNote': 'This skill describes interfaces and safeguards; it does not contain access credentials or runnable third-party integrations.',
        'connectors': ['mcp-server'],
    },
    {
        'slug': 'ml-evaluation-and-fairness',
        'name': 'ML Evaluation and Fairness',
        'level': 'Intermediate',
        'category': 'Quality and governance',
        'summary': 'Measure model quality, generalization, production behavior, and fairness before relying on an AI system.',
        'uses': ['Use when selecting metrics for a model or agent.', 'Use when monitoring drift and production quality.', 'Use when reviewing bias, subgroup performance, and responsible deployment risks.'],
        'capabilities': ['Metric selection', 'Train/test discipline', 'Error analysis', 'Fairness review', 'Production monitoring'],
        'workflow': ['Define the decision, population, and acceptable error trade-offs.', 'Create a representative evaluation set and keep it separate from tuning data.', 'Report precision, recall, calibration, latency, cost, and subgroup performance where relevant.', 'Test robustness, distribution shift, safety, and human escalation paths.', 'Document limitations and establish a review cadence.'],
        'sources': [
            {'title': 'Google Machine Learning Crash Course', 'url': 'https://developers.google.com/machine-learning/crash-course', 'license': 'Public Google developer course; retain the source link and applicable terms.'},
            {'title': 'Google ML Crash Course — fairness', 'url': 'https://developers.google.com/machine-learning/crash-course/fairness', 'license': 'Public Google developer course; use derived guidance with attribution.'},
        ],
        'archiveNote': 'This is a derived evaluation checklist, not a replacement for a model-specific validation protocol.',
        'connectors': [],
    },
    {
        'slug': 'production-agent-security',
        'name': 'Production Agent Security',
        'level': 'Advanced',
        'category': 'Security and operations',
        'summary': 'Deploy agents with least privilege, auditability, safe tool boundaries, secret hygiene, and incident response.',
        'uses': ['Use before connecting an agent to production data or mutating tools.', 'Use when reviewing a skill or connector from an unknown source.', 'Use when setting up logging, key rotation, or emergency revocation.'],
        'capabilities': ['Threat modeling', 'Least privilege', 'Secret lifecycle', 'Audit logging', 'Revocation and recovery'],
        'workflow': ['Inventory data, tools, credentials, and possible side effects.', 'Grant the minimum permissions required for each task.', 'Keep secrets out of skill files, source code, logs, prompts, and client bundles.', 'Record tool access and security events without logging secret values.', 'Rotate, expire, revoke, and test recovery procedures for credentials.', 'Audit every bundled script and external dependency before activation.'],
        'sources': [
            {'title': 'OWASP Secrets Management Cheat Sheet', 'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'license': 'OWASP guidance; retain attribution and verify current terms.'},
            {'title': 'Claude Agent Skills security considerations', 'url': 'https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview', 'license': 'Official documentation; use source links rather than copying proprietary text.'},
            {'title': 'Microsoft AI Agents for Beginners repository', 'url': 'https://github.com/microsoft/ai-agents-for-beginners', 'license': 'MIT repository; verify the LICENSE file for copied code or text.'},
        ],
        'archiveNote': 'Security guidance is intentionally conservative. External skills should be audited like software, not trusted because they are labeled educational.',
        'connectors': ['secrets-vault', 'audit-log'],
    },
    {
        'slug': 'api-integration-and-secrets',
        'name': 'API Integration and Secrets',
        'level': 'Intermediate',
        'category': 'Connectors',
        'summary': 'Document API requirements safely while keeping secret values in a protected server-side environment.',
        'uses': ['Use when an agent skill needs an external API.', 'Use when publishing a connector catalog for humans or agents.', 'Use when replacing a leaked, expired, or over-permissioned key.'],
        'capabilities': ['API contract mapping', 'Credential-name references', 'Scope planning', 'Key rotation', 'Failure-safe integration'],
        'workflow': ['Record the provider, endpoint family, required scopes, rate limits, and data handling rules.', 'Reference a credential by environment-variable or vault name only.', 'Use restricted or read-only credentials when possible.', 'Keep secret values server-side and out of public pages, skills, prompts, logs, and repositories.', 'Define expiration, rotation, revocation, monitoring, and incident-response steps.'],
        'sources': [
            {'title': 'Stripe secret API key best practices', 'url': 'https://docs.stripe.com/keys-best-practices', 'license': 'Official Stripe documentation; retain source link and do not copy real credentials.'},
            {'title': 'OWASP Secrets Management Cheat Sheet', 'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'license': 'OWASP guidance; retain attribution and verify current terms.'},
            {'title': 'Model Context Protocol introduction', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'Open protocol documentation; check current source terms.'},
        ],
        'archiveNote': 'This catalog stores connector metadata, never API key values.',
        'connectors': ['provider-api', 'secrets-vault'],
    },
]


skills.extend([
    {
        'slug': 'prompt-and-context-engineering', 'name': 'Prompt and Context Engineering', 'level': 'Beginner', 'category': 'Foundations',
        'summary': 'Shape instructions, context, examples, and constraints so an agent produces reliable, bounded work.',
        'uses': ['Use when an agent is vague, inconsistent, or overconfident.', 'Use when designing system instructions and reusable task templates.'],
        'capabilities': ['Instruction hierarchy', 'Context selection', 'Few-shot examples', 'Output schemas', 'Constraint design'],
        'workflow': ['State the task, audience, output, and success criteria.', 'Provide only relevant context and define source priority.', 'Give examples for ambiguous formats or edge cases.', 'Require structured outputs when downstream software will consume results.', 'Test adversarial, incomplete, and out-of-scope requests.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Context Engineering', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/12-context-engineering', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived workflow summary; it does not reproduce the lesson.', 'connectors': []
    },
    {
        'slug': 'agent-planning', 'name': 'Agent Planning Patterns', 'level': 'Intermediate', 'category': 'Reasoning workflows',
        'summary': 'Break complex goals into observable steps, dependencies, checkpoints, and recovery paths.',
        'uses': ['Use when a task has multiple dependent actions.', 'Use when the agent must pause, resume, or explain progress.'],
        'capabilities': ['Task decomposition', 'Dependency mapping', 'Checkpoints', 'Replanning', 'Progress reporting'],
        'workflow': ['Define the final deliverable and acceptance conditions.', 'Break the goal into minimal verifiable steps.', 'Identify dependencies, permissions, and irreversible actions.', 'Execute one bounded step at a time and inspect results.', 'Replan only when evidence changes the path.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Planning Design', 'url': 'https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/what-is-the-ai-agent-planning-design-pattern/', 'license': 'Microsoft Learn source; retain attribution and link.'}],
        'archiveNote': 'Derived planning checklist for agent workflows.', 'connectors': []
    },
    {
        'slug': 'multi-agent-orchestration', 'name': 'Multi-Agent Orchestration', 'level': 'Advanced', 'category': 'Agent architecture',
        'summary': 'Coordinate specialized agents with explicit roles, handoffs, shared artifacts, and a final synthesis step.',
        'uses': ['Use when independent research or judgment can run in parallel.', 'Use when one agent should not hold the entire task context.'],
        'capabilities': ['Role design', 'Parallel fan-out', 'Map-reduce synthesis', 'Failure collection', 'Handoff contracts'],
        'workflow': ['Define one bounded responsibility per agent.', 'Give every agent the same structured output contract.', 'Run independent work in parallel only when state does not conflict.', 'Collect successful and failed results explicitly.', 'Use one reducer to synthesize without silently discarding gaps.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Multi-AI Agent Systems', 'url': 'https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/how-to-use-a-multi-ai-agent-system/', 'license': 'Microsoft Learn source; retain attribution and link.'}],
        'archiveNote': 'Derived orchestration pattern; it does not include a hidden agent network or credentials.', 'connectors': []
    },
    {
        'slug': 'agent-memory', 'name': 'Agent Memory', 'level': 'Intermediate', 'category': 'Agent architecture',
        'summary': 'Decide what an agent should remember, where it should live, how long it should persist, and how it can be corrected.',
        'uses': ['Use when an agent needs continuity across tasks.', 'Use when memory could contain personal, confidential, or stale information.'],
        'capabilities': ['Working memory', 'Long-term memory', 'Retrieval policy', 'Consent and deletion', 'Memory validation'],
        'workflow': ['Classify information as ephemeral, session, user, or organizational memory.', 'Store only information with a clear future-use justification.', 'Attach source, date, confidence, and owner metadata.', 'Let users inspect, correct, export, and delete memory where applicable.', 'Expire stale or unverified memory and test retrieval quality.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Agent Memory', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/13-agent-memory', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived memory-governance workflow; storage implementation remains application-specific.', 'connectors': ['document-store']
    },
    {
        'slug': 'browser-use', 'name': 'Browser Use', 'level': 'Advanced', 'category': 'Tool use',
        'summary': 'Use web browsers safely for navigation, extraction, and reversible interactions while respecting user boundaries.',
        'uses': ['Use when information or workflows exist only in a dynamic web app.', 'Use when a browser action needs careful confirmation or takeover.'],
        'capabilities': ['Page navigation', 'Form interpretation', 'State inspection', 'User takeover', 'Action confirmation'],
        'workflow': ['Identify the exact page, goal, and consequences of the action.', 'Read visible page state before clicking or submitting.', 'Treat login, payment, legal, medical, government, and destructive steps as protected workflows.', 'Ask for user takeover when secret input or manual interaction is required.', 'Verify the result and report what changed.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Browser Use', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/15-browser-use', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived browser safety workflow; it does not grant access to any user account.', 'connectors': ['web-search']
    },
    {
        'slug': 'llm-fundamentals', 'name': 'LLM Fundamentals', 'level': 'Beginner', 'category': 'Model literacy',
        'summary': 'Explain tokens, embeddings, Transformers, generation limits, and practical model behavior to agent builders.',
        'uses': ['Use when choosing a model or explaining model limitations.', 'Use when designing prompts, context windows, and evaluation examples.'],
        'capabilities': ['Tokenization', 'Embeddings', 'Transformer concepts', 'Generation behavior', 'Model limitations'],
        'workflow': ['Define the task and the model capability it needs.', 'Estimate context, output, latency, and cost requirements.', 'Distinguish learned patterns from verified external facts.', 'Test representative inputs, edge cases, and refusal behavior.', 'Document model version and assumptions.'],
        'sources': [{'title': 'Google ML Crash Course — Intro to Large Language Models', 'url': 'https://developers.google.com/machine-learning/crash-course/llm', 'license': 'Public Google developer course; retain the source link and applicable terms.'}],
        'archiveNote': 'Derived model-literacy notes; not a copy of the course module.', 'connectors': []
    },
    {
        'slug': 'embeddings-and-semantic-search', 'name': 'Embeddings and Semantic Search', 'level': 'Intermediate', 'category': 'Knowledge retrieval',
        'summary': 'Represent text as vectors and retrieve semantically related material while measuring relevance and failure cases.',
        'uses': ['Use when keyword search misses relevant concepts.', 'Use when building a retrieval layer for documents or skills.'],
        'capabilities': ['Chunking', 'Vector representations', 'Similarity search', 'Metadata filters', 'Retrieval evaluation'],
        'workflow': ['Define the retrieval unit and metadata fields.', 'Chunk documents without destroying meaning or citation boundaries.', 'Generate embeddings with a versioned model.', 'Combine semantic similarity with filters and keyword signals.', 'Evaluate recall, precision, citation coverage, and stale-content behavior.'],
        'sources': [{'title': 'Google ML Crash Course — Embeddings', 'url': 'https://developers.google.com/machine-learning/crash-course/embeddings', 'license': 'Public Google developer course; retain the source link and applicable terms.'}],
        'archiveNote': 'Derived retrieval workflow; vector stores and embedding keys are connector-specific.', 'connectors': ['document-store']
    },
    {
        'slug': 'classification-and-regression', 'name': 'Classification and Regression', 'level': 'Beginner', 'category': 'Machine learning',
        'summary': 'Choose supervised-learning targets, features, metrics, and thresholds for prediction tasks.',
        'uses': ['Use when an agent must score, classify, or predict from structured data.', 'Use when comparing model errors and business trade-offs.'],
        'capabilities': ['Target definition', 'Feature preparation', 'Threshold selection', 'Confusion matrices', 'Error analysis'],
        'workflow': ['Define the target and decision impact.', 'Split data without leakage and establish a baseline.', 'Select metrics that reflect the cost of false positives and negatives.', 'Inspect subgroup and slice performance.', 'Calibrate thresholds and monitor changes after deployment.'],
        'sources': [{'title': 'Google ML Crash Course — Classification', 'url': 'https://developers.google.com/machine-learning/crash-course/classification', 'license': 'Public Google developer course; retain the source link and applicable terms.'}, {'title': 'Google ML Crash Course — Linear Regression', 'url': 'https://developers.google.com/machine-learning/crash-course/linear-regression', 'license': 'Public Google developer course; retain the source link and applicable terms.'}],
        'archiveNote': 'Derived model-selection checklist; it is not a substitute for domain validation.', 'connectors': []
    },
    {
        'slug': 'production-ml-systems', 'name': 'Production ML Systems', 'level': 'Advanced', 'category': 'Operations',
        'summary': 'Move models and agent components from experiments into monitored, reproducible, maintainable production systems.',
        'uses': ['Use when an AI prototype must run reliably for users.', 'Use when planning data, model, infrastructure, and rollback responsibilities.'],
        'capabilities': ['Data pipelines', 'Versioning', 'Deployment', 'Monitoring', 'Rollback design'],
        'workflow': ['Define service-level objectives and ownership.', 'Version data, code, prompts, models, and evaluation sets.', 'Automate tests and reproducible builds.', 'Monitor quality, latency, cost, drift, safety, and dependency health.', 'Prepare rollback, incident response, and retraining triggers.'],
        'sources': [{'title': 'Google ML Crash Course — Production ML Systems', 'url': 'https://developers.google.com/machine-learning/crash-course/production-ml-systems', 'license': 'Public Google developer course; retain the source link and applicable terms.'}],
        'archiveNote': 'Derived production checklist; infrastructure credentials are never included.', 'connectors': ['audit-log', 'secrets-vault']
    },
    {
        'slug': 'agent-evaluation-and-observability', 'name': 'Agent Evaluation and Observability', 'level': 'Advanced', 'category': 'Quality and governance',
        'summary': 'Measure whether agents complete tasks correctly, safely, efficiently, and with reproducible evidence.',
        'uses': ['Use before releasing a new agent.', 'Use when agent quality changes after a prompt, model, tool, or data update.'],
        'capabilities': ['Golden tasks', 'Trace review', 'Rubrics', 'Regression tests', 'Cost and latency analysis'],
        'workflow': ['Create a representative evaluation set with expected outcomes.', 'Capture tool traces, sources, intermediate failures, and final outputs.', 'Score correctness, completeness, safety, citation quality, cost, and latency.', 'Compare against baselines and test adversarial cases.', 'Block releases when critical metrics regress.'],
        'sources': [{'title': 'Hugging Face AI Agents Course', 'url': 'https://huggingface.co/learn/agents-course/en/unit0/introduction', 'license': 'Course access is free; use a derived summary rather than copying lesson text.'}, {'title': 'Microsoft AI Agents for Beginners', 'url': 'https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/', 'license': 'Microsoft Learn source; retain attribution and link.'}],
        'archiveNote': 'Derived evaluation workflow; logs should mask secrets and personal data.', 'connectors': ['audit-log']
    },
    {
        'slug': 'agent-deployment', 'name': 'Agent Deployment', 'level': 'Advanced', 'category': 'Operations',
        'summary': 'Package, deploy, health-check, scale, and update agent services with clear runtime boundaries.',
        'uses': ['Use when moving an agent from local development to a hosted service.', 'Use when deploying multiple versions or environments.'],
        'capabilities': ['Runtime configuration', 'Health checks', 'Environment separation', 'Scaling', 'Release rollback'],
        'workflow': ['Separate development, staging, and production resources.', 'Declare runtime configuration without embedding secrets.', 'Add unauthenticated health checks and authenticated application routes.', 'Deploy immutable versions and retain rollback targets.', 'Monitor resource use, errors, latency, and external dependency failures.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Deploying Scalable Agents', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/16-deploying-scalable-agents', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived deployment checklist; actual hosting and credentials remain environment-specific.', 'connectors': ['secrets-vault', 'audit-log']
    },
    {
        'slug': 'local-ai-agents', 'name': 'Local AI Agents', 'level': 'Intermediate', 'category': 'Runtime choices',
        'summary': 'Assess local models and local agent runtimes for privacy, cost, latency, offline use, and hardware constraints.',
        'uses': ['Use when data should remain on a local machine.', 'Use when experimenting without a hosted model endpoint.'],
        'capabilities': ['Model selection', 'Hardware fit', 'Offline operation', 'Local tool access', 'Privacy review'],
        'workflow': ['Classify data sensitivity and connectivity requirements.', 'Measure local memory, throughput, latency, and quality constraints.', 'Select a model and runtime that fit the hardware.', 'Limit filesystem and network permissions.', 'Compare local quality and operating cost with hosted alternatives.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Creating Local AI Agents', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/17-creating-local-ai-agents', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived decision framework; no local model files or private data are bundled.', 'connectors': []
    },
    {
        'slug': 'secure-agent-architecture', 'name': 'Secure Agent Architecture', 'level': 'Advanced', 'category': 'Security and governance',
        'summary': 'Threat-model agent prompts, tools, data, dependencies, and user actions before deployment.',
        'uses': ['Use when an agent can access sensitive data or take external actions.', 'Use when reviewing prompt injection, tool abuse, and data-exfiltration risks.'],
        'capabilities': ['Threat modeling', 'Prompt-injection defense', 'Data boundaries', 'Action authorization', 'Security testing'],
        'workflow': ['Map trust boundaries and assets.', 'Treat retrieved content and external instructions as untrusted data.', 'Validate tool arguments and authorize actions independently of model output.', 'Constrain data access and prevent cross-tenant leakage.', 'Run security tests and document residual risk.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Securing AI Agents', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/18-securing-ai-agents', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}, {'title': 'OWASP Secrets Management Cheat Sheet', 'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'license': 'OWASP guidance; retain attribution and verify current terms.'}],
        'archiveNote': 'Derived security controls; an archive entry does not certify a connector or agent as secure.', 'connectors': ['audit-log', 'secrets-vault']
    },
    {
        'slug': 'microsoft-agent-framework', 'name': 'Microsoft Agent Framework Orientation', 'level': 'Intermediate', 'category': 'Frameworks',
        'summary': 'Map agent concepts to a framework while keeping prompts, tools, state, and evaluation portable.',
        'uses': ['Use when comparing frameworks or onboarding a team.', 'Use when migrating a prototype without losing test coverage.'],
        'capabilities': ['Framework mapping', 'Portable contracts', 'Tool adapters', 'State boundaries', 'Migration planning'],
        'workflow': ['Describe the agent behavior independently of framework syntax.', 'Map model, tool, state, and orchestration abstractions.', 'Keep inputs and outputs schema-based.', 'Build adapters around external services.', 'Run the same evaluation set before and after migration.'],
        'sources': [{'title': 'Microsoft AI Agents for Beginners — Microsoft Agent Framework', 'url': 'https://github.com/microsoft/ai-agents-for-beginners/tree/main/14-microsoft-agent-framework', 'license': 'MIT repository; verify the LICENSE file before copying code or text.'}],
        'archiveNote': 'Derived framework-neutral orientation; it does not endorse one vendor or require a paid account.', 'connectors': []
    },
    {
        'slug': 'responsible-ai-review', 'name': 'Responsible AI Review', 'level': 'Intermediate', 'category': 'Quality and governance',
        'summary': 'Review an AI system for fairness, transparency, privacy, safety, accountability, and human oversight.',
        'uses': ['Use before launching a user-facing AI feature.', 'Use when a model affects eligibility, ranking, safety, or access to services.'],
        'capabilities': ['Impact assessment', 'Fairness review', 'Human oversight', 'Transparency notes', 'Risk register'],
        'workflow': ['Define affected people, decisions, and potential harms.', 'Measure performance across relevant groups and conditions.', 'Document data provenance, limitations, and intended use.', 'Provide appeal, correction, and human-escalation paths.', 'Review incidents and update controls as the system changes.'],
        'sources': [{'title': 'Google ML Crash Course — Fairness', 'url': 'https://developers.google.com/machine-learning/crash-course/fairness', 'license': 'Public Google developer course; retain the source link and applicable terms.'}, {'title': 'Model Context Protocol security guidance', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'Open protocol documentation; check current source terms.'}],
        'archiveNote': 'Derived governance checklist; legal and regulatory review may still be required.', 'connectors': []
    },
    {
        'slug': 'api-contract-design', 'name': 'API Contract Design', 'level': 'Intermediate', 'category': 'Connectors',
        'summary': 'Define stable API inputs, outputs, errors, limits, authentication references, and versioning for agents.',
        'uses': ['Use when exposing a business capability as an agent tool.', 'Use when an API must remain safe and understandable to multiple clients.'],
        'capabilities': ['Schema design', 'Error contracts', 'Idempotency', 'Rate limits', 'Versioning'],
        'workflow': ['Define the smallest useful operation.', 'Specify required and optional fields with examples.', 'Return structured success and failure responses.', 'Document idempotency, pagination, rate limits, and retries.', 'Reference credentials by name and scope, never by value.'],
        'sources': [{'title': 'Model Context Protocol introduction', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'Open protocol documentation; check current source terms.'}, {'title': 'Stripe secret API key best practices', 'url': 'https://docs.stripe.com/keys-best-practices', 'license': 'Official Stripe documentation; retain source link and do not copy real credentials.'}],
        'archiveNote': 'Derived API contract checklist; it does not create or store a provider key.', 'connectors': ['provider-api']
    },
])




skills.extend([
    {
        'slug': 'agent-workflow-patterns', 'name': 'Agent Workflow Patterns', 'level': 'Intermediate', 'category': 'Agent architecture',
        'summary': 'Choose and compose predefined workflow patterns — chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer — before reaching for a fully autonomous agent.',
        'uses': ['Use when a task decomposes into predictable steps that code can orchestrate.', 'Use when deciding between a workflow and an autonomous agent.', 'Use when a prototype agent is unreliable and needs more deterministic structure.'],
        'capabilities': ['Pattern selection', 'Prompt chaining with gates', 'Input routing', 'Parallel sectioning and voting', 'Evaluator-optimizer loops'],
        'workflow': ['Start with a single augmented model call and add structure only when it measurably helps.', 'Map the task to a pattern: fixed sequence, category routing, independent sections, dynamic decomposition, or a critique loop.', 'Put programmatic checks between chained steps so errors stop early.', 'Give the orchestrator a bounded task list and require a synthesis step.', 'Cap evaluator loops and record the best artifact and its rationale.', 'Promote a workflow to an autonomous agent only when the path cannot be specified in advance.'],
        'sources': [{'title': 'LangChain Academy — Introduction to LangGraph', 'url': 'https://github.com/langchain-ai/langchain-academy', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'Anthropic courses repository — Tool use course', 'url': 'https://github.com/anthropics/courses', 'license': 'CC BY-NC 4.0 — derived summaries permitted for this free archive; non-commercial only, so this entry is excluded from any future paid tier.'}],
        'archiveNote': 'Derived pattern summary written for this archive from the linked public course material; the pattern names are a widely used taxonomy, not quoted text.', 'connectors': []
    },
    {
        'slug': 'prompt-evaluation-pipelines', 'name': 'Prompt Evaluation Pipelines', 'level': 'Intermediate', 'category': 'Quality and governance',
        'summary': 'Build repeatable evaluation sets and graders that score prompt quality before and after changes reach production.',
        'uses': ['Use when changing a production prompt, model, or template.', 'Use when prompt quality is currently judged by anecdote.', 'Use when a team needs a shared quality bar across many prompts.'],
        'capabilities': ['Eval set design', 'Grader selection', 'Human review sampling', 'Regression comparison', 'Failure clustering'],
        'workflow': ['Collect representative inputs, including edge cases and known failures.', 'Define what a good output looks like with a rubric or reference answers.', 'Choose graders: exact checks, model-based scoring, human review, or a mix.', 'Run candidate and baseline prompts on the same frozen set.', 'Cluster failures by cause and fix the largest cluster first.', 'Freeze the set and re-run it on every prompt or model change.'],
        'sources': [{'title': 'Anthropic courses repository — Prompt evaluations course', 'url': 'https://github.com/anthropics/courses', 'license': 'CC BY-NC 4.0 — derived summaries permitted for this free archive; non-commercial only, so this entry is excluded from any future paid tier.'}, {'title': 'Hugging Face AI Agents Course', 'url': 'https://huggingface.co/learn/agents-course/unit0/introduction', 'license': 'Apache-2.0 course repository; use a derived summary rather than copying lesson text.'}],
        'archiveNote': 'Derived from public course concepts; grader prompts and datasets from sources are not reproduced.', 'connectors': ['audit-log']
    },
    {
        'slug': 'multimodal-prompting', 'name': 'Multimodal Prompting', 'level': 'Beginner', 'category': 'Model literacy',
        'summary': 'Give models images and documents as evidence, structure what they should look for, and verify visual claims before acting on them.',
        'uses': ['Use when a task involves screenshots, scans, photos, charts, or PDFs.', 'Use when extracting structured facts from visual material.', 'Use when a text-only prompt keeps missing information that is visible.'],
        'capabilities': ['Image grounding', 'Document triage', 'Visual question design', 'Cross-checking claims', 'Uncertainty reporting'],
        'workflow': ['State what the model must find, decide, or extract from the visual input.', 'Order and label multiple images or pages so references stay unambiguous.', 'Ask for observations first and conclusions second.', 'Require the model to point to the visual evidence behind each claim.', 'Verify critical values against the source document or a second pass.', 'Record low-confidence readings for human review instead of guessing.'],
        'sources': [{'title': 'Anthropic courses repository — API fundamentals', 'url': 'https://github.com/anthropics/courses', 'license': 'CC BY-NC 4.0 — derived summaries permitted for this free archive; non-commercial only, so this entry is excluded from any future paid tier.'}, {'title': 'Microsoft Generative AI for Beginners', 'url': 'https://github.com/microsoft/generative-ai-for-beginners', 'license': 'MIT-licensed Microsoft course repository; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived summary of public course concepts; no course exercises are reproduced.', 'connectors': ['document-store']
    },
    {
        'slug': 'openai-agents-sdk', 'name': 'OpenAI Agents SDK Orientation', 'level': 'Intermediate', 'category': 'Frameworks',
        'summary': 'Build agents from a small set of primitives — agents, tools, handoffs, guardrails, sessions, and built-in tracing.',
        'uses': ['Use when standardizing on the OpenAI Agents SDK for a Python or TypeScript service.', 'Use when a prototype built on raw API calls needs structure without a heavy framework.', 'Use when handoffs between specialist agents are the main design problem.'],
        'capabilities': ['Agent configuration', 'Function tools', 'Handoffs and agents-as-tools', 'Input and output guardrails', 'Trace review'],
        'workflow': ['Define each agent with one responsibility, its instructions, and its tools.', 'Model delegation explicitly: handoffs for full transfer, agents-as-tools for bounded subtasks.', 'Add input and output guardrails that run alongside the agent loop.', 'Attach a session store when conversations must persist across runs.', 'Run representative tasks and inspect traces before tuning prompts.', 'Keep a raw-API fallback path for steps the SDK abstracts awkwardly.'],
        'sources': [{'title': 'OpenAI Agents SDK documentation', 'url': 'https://openai.github.io/openai-agents-python/', 'license': 'Official OpenAI documentation for an MIT-licensed SDK; retain source links.'}, {'title': 'OpenAI Cookbook', 'url': 'https://github.com/openai/openai-cookbook', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived orientation summary; SDK APIs change quickly, so verify against the linked documentation.', 'connectors': ['provider-api', 'audit-log']
    },
    {
        'slug': 'structured-data-extraction', 'name': 'Structured Data Extraction', 'level': 'Intermediate', 'category': 'Data workflows',
        'summary': 'Turn unstructured text and documents into validated records using explicit schemas, constrained outputs, and repair loops.',
        'uses': ['Use when converting emails, invoices, forms, or articles into database records.', 'Use when downstream software needs dependable fields, not prose.', 'Use when manual data entry from documents is the bottleneck.'],
        'capabilities': ['Schema design', 'Constrained generation', 'Field validation', 'Repair and retry', 'Extraction evaluation'],
        'workflow': ['Define the record schema with types, required fields, and allowed values.', 'Split long documents so each extraction call sees one coherent unit.', 'Request schema-conformant output and validate it programmatically.', 'On validation failure, return the specific errors to the model for one bounded repair attempt.', 'Measure field-level accuracy on a labeled sample before scaling.', 'Route low-confidence records to human review with the source text attached.'],
        'sources': [{'title': 'OpenAI Cookbook', 'url': 'https://github.com/openai/openai-cookbook', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived workflow; example schemas from sources are not reproduced.', 'connectors': ['document-store', 'provider-api']
    },
    {
        'slug': 'realtime-voice-agents', 'name': 'Realtime Voice Agents', 'level': 'Advanced', 'category': 'Realtime systems',
        'summary': 'Build speech-to-speech agents that manage turns, interruptions, tool calls, and guardrails within a live audio session.',
        'uses': ['Use when an agent must hold a spoken conversation with low latency.', 'Use when phone or in-app voice is the primary interface.', 'Use when text chat prototypes need a voice counterpart with the same tools.'],
        'capabilities': ['Session design', 'Turn and interruption handling', 'Voice tool calling', 'Streaming guardrails', 'Latency budgeting'],
        'workflow': ['Define the session contract: voice, turn-taking behavior, and when the agent may interrupt or be interrupted.', 'Reuse the same tool definitions as the text agent so behavior stays consistent.', 'Stream partial transcripts and tool results so the conversation never stalls silently.', 'Apply guardrails to both the user audio transcript and the agent responses.', 'Budget latency per stage and degrade gracefully to shorter replies under load.', 'Log transcripts, tool calls, and interruptions for quality review with secrets and personal data masked.'],
        'sources': [{'title': 'OpenAI Agents SDK documentation — realtime agents', 'url': 'https://openai.github.io/openai-agents-python/', 'license': 'Official OpenAI documentation for an MIT-licensed SDK; retain source links.'}, {'title': 'OpenAI Cookbook', 'url': 'https://github.com/openai/openai-cookbook', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived design summary; test with real speakers and noisy audio before relying on lab results.', 'connectors': ['provider-api', 'audit-log']
    },
    {
        'slug': 'llm-fine-tuning-workflows', 'name': 'LLM Fine-Tuning Workflows', 'level': 'Intermediate', 'category': 'Machine learning',
        'summary': 'Adapt a model to a narrow task with curated examples, a held-out evaluation, and a rollback plan, instead of tuning on intuition.',
        'uses': ['Use when prompting plateaus on a stable, well-defined task.', 'Use when a smaller tuned model could replace a larger prompted one.', 'Use when consistent formatting or classification behavior matters more than generality.'],
        'capabilities': ['Dataset curation', 'Train/validation splits', 'Run configuration', 'Comparative evaluation', 'Deployment gating'],
        'workflow': ['Confirm the task is stable and that prompt and retrieval fixes are exhausted.', 'Curate examples from real failures and successes; remove duplicates and label noise.', 'Hold out an evaluation set the tuning data never touches.', 'Run the smallest training configuration that can show signal.', 'Compare tuned and base models on the held-out set and on cost and latency.', 'Ship behind a gate with monitoring and a one-step rollback to the base model.'],
        'sources': [{'title': 'OpenAI Cookbook', 'url': 'https://github.com/openai/openai-cookbook', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'Hugging Face AI Agents Course — fine-tuning for function calling', 'url': 'https://huggingface.co/learn/agents-course/unit0/introduction', 'license': 'Apache-2.0 course repository; use a derived summary rather than copying lesson text.'}],
        'archiveNote': 'Derived workflow; it includes no training data or hyperparameters from any source course.', 'connectors': ['provider-api']
    },
    {
        'slug': 'generative-media-generation', 'name': 'Generative Media Generation', 'level': 'Beginner', 'category': 'Generative media',
        'summary': 'Create and edit images with generative models inside an application while handling prompts, safety, and asset provenance deliberately.',
        'uses': ['Use when an app needs illustrations, mockups, or visual variants.', 'Use when editing or extending existing images with a model.', 'Use when generating media at a scale manual design cannot cover.'],
        'capabilities': ['Visual prompt design', 'Image editing workflows', 'Style consistency', 'Safety and rights checks', 'Asset cataloging'],
        'workflow': ['Define the asset: subject, style, dimensions, and where it will be used.', 'Write prompts that specify composition and exclusions, not just subject keywords.', 'Generate variants and select against the brief rather than the first output.', 'Check outputs for artifacts, text errors, likeness, and rights problems.', 'Store the prompt, model, and generation settings with the final asset for reproducibility.', 'Label AI-generated assets where users or regulators expect disclosure.'],
        'sources': [{'title': 'Microsoft Generative AI for Beginners', 'url': 'https://github.com/microsoft/generative-ai-for-beginners', 'license': 'MIT-licensed Microsoft course repository; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived summary of public course concepts; no course images or prompts are reproduced.', 'connectors': ['provider-api']
    },
    {
        'slug': 'small-language-models', 'name': 'Small Language Models', 'level': 'Intermediate', 'category': 'Runtime choices',
        'summary': 'Choose and run small language models for cost, latency, privacy, or offline needs, and verify they are good enough for the assigned task.',
        'uses': ['Use when a frontier model is overkill for classification, extraction, or drafting.', 'Use when inference must run on-device or inside a private network.', 'Use when per-request cost or latency dominates the design.'],
        'capabilities': ['Task-fit assessment', 'Model comparison', 'Local runtime setup', 'Quality spot-checking', 'Escalation routing'],
        'workflow': ['Define the narrow task and the minimum acceptable quality.', 'Benchmark two or three candidate small models on real examples, not vendor demos.', 'Set up the local or hosted runtime with pinned versions and resource limits.', 'Add a router that escalates hard or low-confidence cases to a larger model.', 'Monitor quality drift as inputs change and re-benchmark on a schedule.', 'Document which tasks the small model owns and which it must never take.'],
        'sources': [{'title': 'Microsoft Generative AI for Beginners', 'url': 'https://github.com/microsoft/generative-ai-for-beginners', 'license': 'MIT-licensed Microsoft course repository; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived summary; benchmark figures from any single course should be re-measured on your own workload.', 'connectors': []
    },
    {
        'slug': 'smolagents-code-agents', 'name': 'smolagents Code Agents', 'level': 'Intermediate', 'category': 'Frameworks',
        'summary': 'Build lightweight agents whose actions are Python code, with sandboxed execution, composable tools, and managed sub-agents.',
        'uses': ['Use when an agent benefits from loops, variables, and combined tool calls in one step.', 'Use when a minimal, readable framework is preferable to a large platform.', 'Use when experimenting with code-writing agents before committing to a stack.'],
        'capabilities': ['CodeAgent configuration', 'Tool authoring', 'Sandbox selection', 'Managed agents', 'Run inspection'],
        'workflow': ['Pick CodeAgent for code actions or ToolCallingAgent for native JSON tool calls.', 'Register tools with precise docstrings; the model reads them as its manual.', 'Choose a real sandbox for generated code; the built-in local executor is not a security boundary.', 'Limit authorized imports and steps, and enable planning intervals for long tasks.', 'Add managed agents for specialized subtasks instead of growing one prompt.', 'Inspect runs with traces to find wasted steps and failing tools.'],
        'sources': [{'title': 'smolagents documentation — inspecting runs', 'url': 'https://huggingface.co/docs/smolagents/en/tutorials/inspect_runs', 'license': 'smolagents is Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'Hugging Face AI Agents Course — smolagents unit', 'url': 'https://github.com/huggingface/agents-course/blob/HEAD/units/en/unit2/smolagents/tool_calling_agents.mdx', 'license': 'Apache-2.0 course repository; use a derived summary rather than copying lesson text.'}],
        'archiveNote': 'Derived orientation summary. Never run generated code outside a sandbox you control.', 'connectors': ['provider-api']
    },
    {
        'slug': 'llamaindex-data-agents', 'name': 'LlamaIndex Data Agents', 'level': 'Intermediate', 'category': 'Frameworks',
        'summary': 'Build agents over private data with LlamaIndex indexing, query tools, and workflow events that keep retrieval auditable.',
        'uses': ['Use when an agent must answer and act over a document collection.', 'Use when retrieval quality, not the chat loop, is the hard part.', 'Use when a RAG prototype needs tool use and multi-step workflows.'],
        'capabilities': ['Index design', 'Query engines as tools', 'Workflow events', 'Retrieval evaluation', 'Source attribution'],
        'workflow': ['Inventory the corpus and decide chunking, metadata, and refresh cadence.', 'Build indexes per collection so permissions and provenance stay separable.', 'Expose query engines as named tools with narrow descriptions.', 'Compose multi-step behavior as explicit workflow events rather than hidden chains.', 'Evaluate retrieval separately from answer quality so failures are attributable.', 'Attach source references to every answer the agent produces.'],
        'sources': [{'title': 'Hugging Face AI Agents Course — frameworks unit (LlamaIndex)', 'url': 'https://huggingface.co/learn/agents-course/unit0/introduction', 'license': 'Apache-2.0 course repository; use a derived summary rather than copying lesson text.'}],
        'archiveNote': 'Derived orientation summary; verify current LlamaIndex APIs against the project documentation before building.', 'connectors': ['document-store', 'web-search']
    },
    {
        'slug': 'langgraph-stateful-agents', 'name': 'LangGraph Stateful Agents', 'level': 'Intermediate', 'category': 'Frameworks',
        'summary': 'Model an agent as an explicit graph of nodes and edges over shared state, with checkpointing that makes runs resumable and inspectable.',
        'uses': ['Use when agent behavior needs explicit control flow instead of a free-running loop.', 'Use when runs must pause, resume, or be replayed for debugging.', 'Use when multiple agents and tools share one evolving state.'],
        'capabilities': ['State schema design', 'Nodes and conditional edges', 'Checkpointers and threads', 'Subgraphs', 'State inspection'],
        'workflow': ['Define the state schema first: what accumulates, what gets overwritten, and what stays private to a node.', 'Implement nodes as small functions that return state updates rather than mutating shared state.', 'Wire conditional edges for tool calls, retries, and termination, with a recursion limit.', 'Compile with a checkpointer and a thread id per conversation or task.', 'Inspect saved state at failure points before changing prompts.', 'Promote the checkpointer from in-memory to a durable store for production.'],
        'sources': [{'title': 'LangChain Academy — Introduction to LangGraph', 'url': 'https://github.com/langchain-ai/langchain-academy', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'LangGraph concepts — human-in-the-loop and persistence', 'url': 'https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/', 'license': 'LangChain documentation; retain source links and verify current terms.'}],
        'archiveNote': 'Derived orientation summary based on public course and documentation concepts.', 'connectors': ['audit-log']
    },
    {
        'slug': 'human-in-the-loop-agents', 'name': 'Human-in-the-Loop Agents', 'level': 'Advanced', 'category': 'Agent architecture',
        'summary': 'Pause agent execution at consequential moments so a person can approve, edit, or reject the next action, then resume from saved state.',
        'uses': ['Use before an agent sends, pays, deletes, publishes, or changes records.', 'Use when full automation is possible but not yet trusted.', 'Use when regulations or policy require a human decision in the loop.'],
        'capabilities': ['Interrupt design', 'Approval payloads', 'Edit-and-resume flows', 'Timeout and expiry policy', 'Decision audit trails'],
        'workflow': ['Classify actions by reversibility and blast radius; only consequential ones interrupt.', 'Persist full state at the interrupt so the run can wait indefinitely.', 'Present the reviewer a compact payload: intent, inputs, expected effect, and alternatives.', 'Support approve, edit, and reject as distinct resume values, not a single yes/no.', 'Expire stale approvals and re-validate state before executing an approved action.', 'Log who decided, what changed, and how long review took.'],
        'sources': [{'title': 'LangGraph concepts — human-in-the-loop', 'url': 'https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/', 'license': 'LangChain documentation; retain source links and verify current terms.'}, {'title': 'LangChain Academy — Introduction to LangGraph', 'url': 'https://github.com/langchain-ai/langchain-academy', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}],
        'archiveNote': 'Derived pattern summary. Human review only helps if reviewers get real context and enough time.', 'connectors': ['audit-log']
    },
    {
        'slug': 'mcp-server-development', 'name': 'MCP Server Development', 'level': 'Intermediate', 'category': 'Agent infrastructure',
        'summary': 'Implement a Model Context Protocol server that exposes tools, resources, and prompts with validated inputs and a deliberately chosen transport.',
        'uses': ['Use when wrapping an internal system for use by multiple AI clients.', 'Use when a tool integration should outlive any single agent framework.', 'Use when exposing read-only data separately from mutating actions.'],
        'capabilities': ['Server scaffolding', 'Tool and resource handlers', 'Transport selection', 'Input validation', 'Inspector testing'],
        'workflow': ['Inventory the capabilities and split them into tools (actions), resources (data), and prompts (templates).', 'Define schemas for every input and output before writing handlers.', 'Implement handlers with least-privilege credentials held server-side.', 'Choose stdio for local clients or streamable HTTP for shared deployment, and configure authentication accordingly.', 'Test with the MCP Inspector and at least one real client before release.', 'Version the server and log calls without recording secret values.'],
        'sources': [{'title': 'Model Context Protocol introduction', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'MCP documentation published under CC BY 4.0 (specification repository transitioning from MIT to Apache-2.0); retain attribution.'}],
        'archiveNote': 'Derived build checklist. The protocol evolves through dated revisions; pin the revision you implement.', 'connectors': ['mcp-server', 'secrets-vault']
    },
    {
        'slug': 'mcp-security-practices', 'name': 'MCP Security Practices', 'level': 'Advanced', 'category': 'Security and governance',
        'summary': 'Deploy MCP clients and servers without confused-deputy, token-passthrough, and consent failures that turn a tool protocol into a privilege-escalation path.',
        'uses': ['Use when an MCP server can act with a user or service authority.', 'Use when adding OAuth or remote servers to an agent product.', 'Use when reviewing a third-party MCP server before connecting it.'],
        'capabilities': ['Consent design', 'Token audience validation', 'Session security', 'Tool description review', 'Server allowlisting'],
        'workflow': ['Require explicit, per-server user consent before an agent gains new tools.', 'Bind tokens to the server audience; never pass a token through to downstream APIs.', 'Treat tool descriptions and server metadata as untrusted input that can change between sessions.', 'Pin session identifiers to the authenticated user and protect them like credentials.', 'Allowlist servers for sensitive environments and re-review them on update.', 'Log authorization decisions and provide a one-action disconnect for every server.'],
        'sources': [{'title': 'Model Context Protocol introduction and security guidance', 'url': 'https://modelcontextprotocol.io/introduction', 'license': 'MCP documentation published under CC BY 4.0 (specification repository transitioning from MIT to Apache-2.0); retain attribution.'}, {'title': 'OWASP Secrets Management Cheat Sheet', 'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'license': 'OWASP guidance; retain attribution and verify current terms.'}],
        'archiveNote': 'Derived from public protocol security guidance; re-check the current MCP specification before each deployment.', 'connectors': ['mcp-server', 'secrets-vault', 'audit-log']
    },
    {
        'slug': 'ai-risk-management-framework', 'name': 'AI Risk Management Framework', 'level': 'Intermediate', 'category': 'Quality and governance',
        'summary': 'Run AI risk as a continuous loop — Govern, Map, Measure, Manage — with named owners, a system inventory, and evidence for each decision.',
        'uses': ['Use when an organization needs one shared method for AI risk across teams.', 'Use when agents move from experiments into systems people depend on.', 'Use when customers or regulators ask how AI risk is managed.'],
        'capabilities': ['Governance and ownership', 'System inventory and context mapping', 'Risk measurement plans', 'Treatment and incident response', 'Trustworthiness review'],
        'workflow': ['Govern: name accountable owners, set risk tolerance, and define approval gates.', 'Map: inventory each AI system with its purpose, data, users, and foreseeable misuse.', 'Measure: test performance, bias, robustness, security, and privacy against the mapped risks.', 'Manage: prioritize treatments, document accepted residual risk, and prepare incident response.', 'Apply the generative AI profile where models create content or act autonomously.', 'Repeat on a cadence and after every material change; the loop does not finish.'],
        'sources': [{'title': 'NIST AI Risk Management Framework', 'url': 'https://www.nist.gov/itl/ai-risk-management-framework', 'license': 'Public domain — U.S. federal government publication; the framework is free for voluntary use.'}, {'title': 'NIST AI 100-1 — AI RMF 1.0 publication', 'url': 'https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10', 'license': 'NIST publication page; NIST-authored content is a U.S. government work (public domain).'}],
        'archiveNote': 'Derived operational summary of a voluntary framework; it is not legal or compliance advice.', 'connectors': ['audit-log']
    },
    {
        'slug': 'llm-threat-controls', 'name': 'LLM Threat Controls', 'level': 'Advanced', 'category': 'Security and governance',
        'summary': 'Defend an LLM application against the OWASP Top 10 risks — prompt injection, sensitive disclosure, excessive agency, unsafe outputs, and unbounded consumption — with layered controls.',
        'uses': ['Use when threat-modeling a chatbot, RAG system, or agent before launch.', 'Use when a security review needs a shared vocabulary for LLM-specific risks.', 'Use when an incident suggests model behavior, not code, was the attack path.'],
        'capabilities': ['Threat enumeration', 'Injection defenses', 'Output handling controls', 'Agency limits', 'Consumption budgets'],
        'workflow': ['Walk the current OWASP LLM Top 10 and mark which risks the system actually exposes.', 'Treat all retrieved and tool-returned text as untrusted data, never as instructions.', 'Validate and encode model output before it reaches browsers, shells, databases, or APIs.', 'Bound agency: least-privilege tools, human approval for irreversible actions, and per-task scopes.', 'Set token, cost, and rate budgets with alerts so consumption attacks surface early.', 'Re-run the review after model, prompt, tool, or data changes and record residual risks.'],
        'sources': [{'title': 'OWASP Top 10 for LLM Applications', 'url': 'https://genai.owasp.org/llm-top-10/', 'license': 'OWASP GenAI Security Project guidance (CC BY-SA 4.0, share-alike); retain attribution and verify the current edition.'}, {'title': 'OWASP Secrets Management Cheat Sheet', 'url': 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'license': 'OWASP guidance; retain attribution and verify current terms.'}],
        'archiveNote': 'Derived control checklist. Rankings change between editions; cite the edition you assessed against.', 'connectors': ['audit-log', 'secrets-vault']
    },
])


skills.extend([
    {
        'slug': 'context-engineering-in-practice', 'name': 'Context Engineering in Practice', 'level': 'Advanced', 'category': 'Agent architecture',
        'summary': 'Manage an agent\u2019s context window as a working set \u2014 write, select, compress, and isolate \u2014 so long tasks stay accurate, cache-friendly, and affordable.',
        'uses': ['Use when an agent degrades on long tasks as tool output floods its context.', 'Use when context cost or latency grows faster than the value of the work.', 'Use when designing how sub-agents share \u2014 or deliberately do not share \u2014 context.'],
        'capabilities': ['Context budgeting', 'Write/select/compress/isolate strategies', 'KV-cache hygiene', 'Tool masking', 'Sub-agent isolation'],
        'workflow': ['Inventory every source that competes for the window (instructions, history, tool results, retrieved knowledge) and what each costs.', 'Write durable state outside the window \u2014 scratchpads, files, structured state \u2014 and re-read it on demand.', 'Select just-in-time: retrieve knowledge and tools when a step needs them instead of preloading everything.', 'Compress at task checkpoints: summarize history while preserving decisions, artifacts, and open questions.', 'Isolate work in sub-agents with narrow context that return condensed results, and treat shared writes as a deliberate exception.', 'Keep the static prefix byte-stable so provider caches hit, and mask tools instead of removing them so cached context stays valid.'],
        'sources': [{'title': 'Context Engineering for Agents \u2014 Lance Martin, LangChain (video)', 'url': 'https://www.youtube.com/watch?v=_IlTcWciEC4', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Context Engineering for AI Agents, with Manus \u2014 LangChain (video)', 'url': 'https://www.youtube.com/watch?v=6_BcCthVvb8', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Cole Medin \u2014 context-engineering-intro repository', 'url': 'https://github.com/coleam00/context-engineering-intro', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'LangChain context engineering notebooks', 'url': 'https://github.com/langchain-ai/context_engineering', 'license': 'Companion notebooks for the LangChain talk; no LICENSE file in the repository \u2014 concepts summarized only, no code or text reproduced.'}],
        'archiveNote': 'Derived practice summary from the linked talks and public repositories; no transcript or notebook text is reproduced.', 'connectors': ['document-store']
    },
    {
        'slug': 'tiered-agent-memory', 'name': 'Tiered Agent Memory', 'level': 'Advanced', 'category': 'Agent architecture',
        'summary': 'Build long-running agent memory as tiers \u2014 in-context core blocks, recall history, and archival storage \u2014 that the agent pages, edits, and consolidates itself.',
        'uses': ['Use when an agent must remember users, facts, and prior work across sessions.', 'Use when conversations or task histories outgrow the context window.', 'Use when personalization needs memory that a human can inspect and correct.'],
        'capabilities': ['Memory tiers', 'Self-editing memory blocks', 'Paging and eviction', 'Archival search', 'Memory consolidation'],
        'workflow': ['Define the tiers (core in-context blocks, recall history, archival store) and what belongs in each.', 'Expose memory to the agent as explicit read/write tools so every change is an auditable action.', 'Set a context-pressure policy: when the window fills, summarize and page material out to archival storage instead of truncating blindly.', 'Give the agent archival and recall search so paged-out material stays reachable.', 'Consolidate offline: merge duplicates, resolve contradictions, and expire stale entries on a schedule.', 'Evaluate with long-horizon probes for recall accuracy and stale-fact errors, and audit what the agent has stored.'],
        'sources': [{'title': 'Letta (formerly MemGPT) repository', 'url': 'https://github.com/letta-ai/letta', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'Stateful Agents \u2014 Charles Packer, Letta (AI Engineer talk, video)', 'url': 'https://www.youtube.com/watch?v=E0k9Ppq6yXY', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'MemGPT: Towards LLMs as Operating Systems (paper)', 'url': 'https://arxiv.org/abs/2310.08560', 'license': 'Research paper on arXiv; concepts summarized, no text reproduced.'}],
        'archiveNote': 'Derived architecture summary; memory contents are user data and never part of this archive.', 'connectors': ['document-store']
    },
    {
        'slug': 'pipeline-voice-agents', 'name': 'Pipeline Voice Agents', 'level': 'Intermediate', 'category': 'Realtime systems',
        'summary': 'Build voice agents as a streaming cascade \u2014 voice activity detection, speech-to-text, an agent core, and text-to-speech \u2014 with explicit latency budgets and interruption handling.',
        'uses': ['Use when each voice stage must be chosen, measured, or swapped independently.', 'Use when adding voice to an existing text agent without rewriting its logic.', 'Use when telephony (SIP/WebSocket) or local and open models are requirements.'],
        'capabilities': ['Pipeline composition', 'Endpointing and barge-in', 'Latency budgeting', 'Telephony integration', 'Voice tracing'],
        'workflow': ['Choose the cascaded pipeline over speech-to-speech deliberately: control and observability per stage versus raw latency.', 'Assemble stages as stream processors (transport, VAD, STT, agent, TTS) with frames flowing between them.', 'Tune voice activity detection and endpointing so turns end naturally and callers can interrupt (barge-in) without losing the thread.', 'Adapt the agent core to voice: make it session-scoped or stateless per turn and keep responses speakable and short.', 'Instrument per-stage latency and word-error rates, set a total response budget, and trace full calls.', 'Test with real noise, accents, crosstalk, and interruptions before trusting lab results.'],
        'sources': [{'title': 'Pipecat repository (Daily)', 'url': 'https://github.com/pipecat-ai/pipecat', 'license': 'BSD 2-Clause open source; this summary is derived, not copied.'}, {'title': 'LiveKit Agents repository', 'url': 'https://github.com/livekit/agents', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'Turn Any LangGraph Agent Into a Voice Agent \u2014 LangChain (video)', 'url': 'https://www.youtube.com/watch?v=i_Tf956Yh0U', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Build Advanced AI Agents with LiveKit \u2014 freeCodeCamp (video course)', 'url': 'https://www.youtube.com/watch?v=B0TJC4lmzEM', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}],
        'archiveNote': 'Derived design summary for cascaded voice pipelines; it complements, and does not replace, the speech-to-speech entry in this archive.', 'connectors': ['provider-api', 'audit-log']
    },
    {
        'slug': 'error-analysis-for-agents', 'name': 'Error Analysis for AI Agents', 'level': 'Intermediate', 'category': 'Quality and governance',
        'summary': 'Find what is actually broken by reading real agent traces, coding failures into a taxonomy, counting them, and letting the counts \u2014 not intuition \u2014 choose the fixes and the evals.',
        'uses': ['Use when agent quality has plateaued and nobody can say why.', 'Use when deciding which evaluation to build next.', 'Use after launch, when real traffic replaces test scenarios.'],
        'capabilities': ['Trace sampling', 'Open and axial coding', 'Failure taxonomies', 'Judge validation', 'Failure prioritization'],
        'workflow': ['Sample around a hundred real traces, including successes, from production or realistic use.', 'Read each trace and write a one-sentence note naming the first upstream failure (open coding).', 'Group the notes into a failure taxonomy (axial coding) and count how often each mode occurs.', 'Build binary pass/fail judges only for the most frequent failure modes \u2014 one judge per failure, never a generic quality score.', 'Validate each judge against human labels using true-positive and true-negative rates, not raw agreement, and iterate until it tracks the humans.', 'Fix the most frequent upstream failure first, then repeat the loop; for agents, decompose failures by step (transition analysis) to find where runs leave the rails.'],
        'sources': [{'title': 'Evals, Error Analysis, and Better Prompts \u2014 Hamel Husain on How I AI (video)', 'url': 'https://www.youtube.com/watch?v=PgzOBNse2EA', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'How to Build AI Evals \u2014 Hamel Husain and Shreya Shankar (video walkthrough)', 'url': 'https://www.youtube.com/watch?v=J7N9FMouSKg', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}],
        'archiveNote': 'Derived method summary from the linked talks; no transcript text is reproduced. Error analysis is product work \u2014 a domain expert should own the labels.', 'connectors': ['audit-log']
    },
    {
        'slug': 'agent-benchmarking', 'name': 'Agent Benchmarking', 'level': 'Advanced', 'category': 'Quality and governance',
        'summary': 'Design and read agent benchmarks honestly \u2014 executable task suites with deterministic resets, state-based graders, and consistency metrics \u2014 instead of trusting headline scores.',
        'uses': ['Use when comparing agents or models for a real workload.', 'Use when building an internal task suite that mirrors your product.', 'Use when a public leaderboard claim needs scrutiny before it drives a decision.'],
        'capabilities': ['Task suite design', 'Executable grading', 'Environment fidelity', 'Consistency metrics', 'Contamination control'],
        'workflow': ['Define tasks from real work, each with an unambiguous, checkable end state.', 'Make environments resettable and reproducible, and grade from final state (files, database, UI) rather than from the transcript.', 'For conversational agents, add a simulated user with a policy to follow, and verify both the dialogue constraints and the end state.', 'Run multiple trials and report pass@k (any success) alongside pass^k (success on every trial) so consistency is visible, not hidden.', 'Hold out refreshed and private tasks, and rotate them, to detect contamination and overfitting to the suite.', 'Publish cost, latency, step counts, and failure breakdowns next to every score.'],
        'sources': [{'title': 'SWE-bench repository', 'url': 'https://github.com/princeton-nlp/SWE-bench', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'tau-bench repository (Sierra)', 'url': 'https://github.com/sierra-research/tau-bench', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'OSWorld repository (XLANG Lab)', 'url': 'https://github.com/xlang-ai/OSWorld', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}],
        'archiveNote': 'Derived summary of benchmark design practice from the linked open benchmark repositories; benchmark tasks and data are not reproduced.', 'connectors': []
    },
    {
        'slug': 'computer-use-agents', 'name': 'Computer Use Agents', 'level': 'Advanced', 'category': 'Tool use',
        'summary': 'Build agents that operate real desktop software through screenshots and accessibility trees, with coordinate grounding, sandboxed virtual machines, and execution-based evaluation.',
        'uses': ['Use when a task exists only in GUI applications with no usable API.', 'Use when automating legacy desktop or cross-application workflows.', 'Use when measuring a model\u2019s desktop competence before trusting it near real machines.'],
        'capabilities': ['Observation design', 'Visual grounding', 'Action spaces', 'VM sandboxing', 'Execution-based evaluation'],
        'workflow': ['Choose the observation mode \u2014 screenshot, accessibility tree, set-of-marks overlay, or a combination \u2014 and measure the accuracy trade-off on your tasks.', 'Define a small, reliable action space (click, type, scroll, keypress, wait) and ground every action to a visible element.', 'Run the agent inside a disposable virtual machine with snapshots, synthetic data, and no real credentials.', 'Re-observe after every action; treat text trajectory history as the memory, not a growing stack of screenshots.', 'Include feasible tasks and deliberately infeasible ones so refusal and clarification behavior are tested, and gate real-account actions behind human confirmation.', 'Evaluate from final machine state with execution-based checks, and budget steps, time, and cost per task.'],
        'sources': [{'title': 'OSWorld repository (XLANG Lab)', 'url': 'https://github.com/xlang-ai/OSWorld', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'OSWorld project page and paper (NeurIPS 2024)', 'url': 'http://osworld-v1.xlang.ai/', 'license': 'Project page of the Apache-2.0 OSWorld project; findings summarized, no text reproduced.'}],
        'archiveNote': 'Derived summary from the OSWorld benchmark and its published analysis; never point a computer-use agent at real accounts without human confirmation gates.', 'connectors': []
    },
])

skills.extend([
    {
        'slug': 'agent-red-teaming', 'name': 'Agent Red Teaming', 'level': 'Advanced', 'category': 'Security and governance',
        'summary': 'Probe an AI system the way an adversary would \u2014 scripted single- and multi-turn attacks with converters, scorers, and repeatable campaigns \u2014 before someone less friendly does.',
        'uses': ['Use for a pre-launch security assessment of a chatbot, RAG system, or agent.', 'Use when testing whether guardrails survive adaptive, multi-turn attacks rather than single prompts.', 'Use to regression-test safety after a model, prompt, or tool change.'],
        'capabilities': ['Objective definition', 'Attack orchestration', 'Prompt converters', 'Scoring and attack success rate', 'Campaign regression'],
        'workflow': ['Define objectives, harm categories, and scope in writing, with authorization for the target system \u2014 red teaming is sanctioned testing, not improvisation.', 'Map the surface with single-turn probe datasets across categories (leakage, manipulation, policy bypass, agent tool abuse).', 'Escalate to multi-turn strategies \u2014 gradual escalation, branching attacks \u2014 against the weakest categories, because agents fail across turns, not just within one.', 'Apply converters (encodings, translations, obfuscation, persona shifts) to test how deep the defenses go.', 'Score every response with human or model judges and track attack success rate per category, not a single global number.', 'Store campaigns as reusable datasets and re-run them after every fix or model change, diffing results before shipping.'],
        'sources': [{'title': 'Microsoft PyRIT repository', 'url': 'https://github.com/microsoft/PyRIT', 'license': 'MIT License; verify the LICENSE file for copied code or text.'}, {'title': 'AI Red Teaming 101 \u2014 Microsoft AI Red Team course (video series)', 'url': 'https://www.youtube.com/watch?v=DwFVhFdD2fs', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'NVIDIA garak repository', 'url': 'https://github.com/NVIDIA/garak', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}],
        'archiveNote': 'Derived practice summary for authorized testing only; attack prompts and datasets from the sources are not reproduced.', 'connectors': ['audit-log']
    },
    {
        'slug': 'runtime-guardrails', 'name': 'Runtime Guardrails', 'level': 'Intermediate', 'category': 'Security and governance',
        'summary': 'Enforce policy at runtime with programmable rails \u2014 input, dialog, retrieval, execution, and output \u2014 that check, steer, or block LLM behavior independently of the model\u2019s own alignment.',
        'uses': ['Use when a chatbot or agent must stay on-topic and in-policy under adversarial users.', 'Use when tool calls need argument validation before anything executes.', 'Use when RAG answers must be grounded in retrieved evidence before reaching users.'],
        'capabilities': ['Rail design', 'Dialog flows (Colang)', 'Self-check classifiers', 'Grounding checks', 'Latency-aware enforcement'],
        'workflow': ['Write the policy as explicit rails separated by stage: input, dialog, retrieval, execution, and output.', 'Implement cheap deterministic checks first (patterns, allowlists, schema validation) and reserve model-based self-checks for ambiguous cases.', 'Validate tool-call arguments in execution rails before any side effect runs.', 'Buffer streamed output when output rails must inspect a complete response before release.', 'Log every rail trigger with its reason, and tune false positives on real traffic \u2014 a guardrail users route around is not a control.', 'Measure the latency and cost the rails add, and attack-test them with the same adversarial sets used for red teaming.'],
        'sources': [{'title': 'NVIDIA NeMo Guardrails repository', 'url': 'https://github.com/NVIDIA-NeMo/Guardrails', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'NeMo Guardrails documentation (in the same repository)', 'url': 'https://github.com/nvidia/nemo-guardrails/blob/HEAD/docs/reference/cli/index.mdx', 'license': 'Documentation shipped with the Apache-2.0 repository; concepts summarized, no text reproduced.'}],
        'archiveNote': 'Derived implementation summary; guardrails are one layer of defense, not a guarantee of safe behavior.', 'connectors': ['audit-log']
    },
    {
        'slug': 'agent-cost-optimization', 'name': 'Agent Cost Optimization', 'level': 'Intermediate', 'category': 'Operations',
        'summary': 'Cut agent inference cost with measurement first, then the levers that actually move it: cache-stable prompts, model routing and cascades, semantic caching, context pruning, and hard budgets.',
        'uses': ['Use when an agent\u2019s per-task cost is unknown, or climbing faster than usage.', 'Use when long multi-turn sessions get quadratically more expensive.', 'Use when choosing between hosted models, smaller models, and self-hosting.'],
        'capabilities': ['Cost accounting', 'Prompt-cache hygiene', 'Model routing', 'Semantic caching', 'Budget enforcement'],
        'workflow': ['Instrument cost per run, per step, and per successful task before optimizing anything \u2014 and keep quality metrics next to cost in the same dashboard.', 'Keep system prompts, tool definitions, and few-shot blocks byte-stable so provider prefix caches hit, and push dynamic content as late in the prompt as possible.', 'Route by difficulty: small models for easy steps, cascades that escalate only on low confidence, and measure quality per tier so routing never silently degrades output.', 'Add semantic caching for repeated or near-duplicate questions, and batch APIs for work that is not interactive.', 'Cap output tokens, prune accumulated context, and summarize history on long tasks \u2014 history is usually the largest line item.', 'Set per-agent budgets and alerts with a kill switch, and re-run the eval suite after every cost change so savings are never bought with silent quality loss.'],
        'sources': [{'title': 'RouteLLM repository (LMSYS)', 'url': 'https://github.com/lm-sys/RouteLLM', 'license': 'Apache-2.0 open source; this summary is derived, not copied.'}, {'title': 'LiteLLM repository (BerriAI)', 'url': 'https://github.com/BerriAI/litellm', 'license': 'MIT License for the open-source core (the enterprise/ directory carries separate terms); verify the LICENSE file for copied code or text.'}, {'title': 'AI Engineer Masterclass \u2014 Cut Your AI Bill (video)', 'url': 'https://www.youtube.com/watch?v=RoD2JE9LN_w', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Prefix Caching for LLM cost reduction \u2014 practitioner walkthrough (video)', 'url': 'https://www.youtube.com/watch?v=9u83yR1YxwE', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}],
        'archiveNote': 'Derived optimization playbook; savings figures quoted by any single source are workload-specific \u2014 re-measure on your own traffic.', 'connectors': ['provider-api', 'audit-log']
    },
    {
        'slug': 'mcp-in-production', 'name': 'MCP in Production', 'level': 'Advanced', 'category': 'Agent infrastructure',
        'summary': 'Run MCP servers as shared production services \u2014 remote streamable-HTTP transport, OAuth authorization, stateless scaling, monitoring, and versioning that real clients can rely on.',
        'uses': ['Use when graduating a local stdio MCP server to a team or public service.', 'Use when web-based agents (not just desktop clients) need your tools.', 'Use when operating MCP alongside existing APIs without duplicating them badly.'],
        'capabilities': ['Remote transport', 'OAuth 2.1 authorization', 'Stateless scaling', 'Server observability', 'Version and client compatibility'],
        'workflow': ['Move from stdio to the streamable HTTP transport, and decide explicitly what session state exists and where it lives.', 'Put authorization in front: OAuth 2.1 with scoped tokens and per-user consent, and never forward client tokens to downstream APIs.', 'Deploy statelessly where possible so any instance can serve any request; use durable execution for long-running tool calls.', 'Instrument tool calls with tracing, error rates, and latency, and alert on client-visible failures, not just server errors.', 'Version tools additively, publish a changelog, and test against the major MCP clients before each release.', 'Design tools like APIs \u2014 narrow, deterministic, few in number \u2014 with clear input schemas, rather than one tool per internal endpoint.'],
        'sources': [{'title': 'Build and Ship Any MCP Server \u2014 Cole Medin (video)', 'url': 'https://www.youtube.com/watch?v=Zw3sfAIpeH8', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'MCP transports documentation', 'url': 'https://modelcontextprotocol.io/docs/concepts/transports', 'license': 'MCP documentation (CC BY 4.0); this archive records concepts, not copied passages.'}, {'title': 'MCP Demo Day \u2014 Cloudflare engineering blog', 'url': 'https://blog.cloudflare.com/mcp-demo-day/', 'license': 'Cloudflare engineering blog; production patterns summarized, no text reproduced.'}],
        'archiveNote': 'Derived operations summary; the MCP authorization specification is still evolving \u2014 re-check it before each deployment.', 'connectors': ['mcp-server', 'secrets-vault', 'audit-log']
    },
    {
        'slug': 'agent-ux-patterns', 'name': 'Agent UX Patterns', 'level': 'Intermediate', 'category': 'Agent UX',
        'summary': 'Design interfaces that keep people oriented and in control while an agent works: visible process, honest confidence, permission slips for consequential actions, and graceful failure.',
        'uses': ['Use when shipping a user-facing agent, copilot, or support automation.', 'Use when an agent UI feels like a black box and users do not trust its output.', 'Use when deciding what an agent may do autonomously versus what needs approval.'],
        'capabilities': ['Capability communication', 'Process visibility', 'Confidence display', 'Approval design', 'Failure recovery UX'],
        'workflow': ['Communicate capabilities and limits up front \u2014 intro, suggested actions, progressive disclosure \u2014 so users ask for what the agent can actually do.', 'Show the agent\u2019s process (current step, sources, working indicator) instead of a bare spinner; silence reads as failure.', 'Present outcomes as diffs or summaries a person can verify quickly, not as raw logs or walls of text.', 'Gate irreversible or external actions behind a clear permission step, keep a prominent stop control, and design checkpoints because most agent actions have no undo.', 'Communicate uncertainty honestly, look up what can be looked up, and ask at most one clarifying question before acting.', 'On failure, preserve completed work, say plainly what happened and why, and offer a retry that skips finished steps.'],
        'sources': [{'title': 'AgentUI \u2014 5 UI Patterns Every AI Agent App Reuses (video)', 'url': 'https://www.youtube.com/watch?v=NHqGTNLuHK8', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Designing Agent UX \u2014 lecture on agent design patterns and trust (video)', 'url': 'https://www.youtube.com/watch?v=9OdJofTenbc', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Google A2UI explainer \u2014 generative UI for agents (video)', 'url': 'https://www.youtube.com/watch?v=AWtIxcPGhkk', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}],
        'archiveNote': 'Derived pattern summary from the linked talks; no transcript text is reproduced. Design as if there is no undo \u2014 for most agent actions, there is not.', 'connectors': []
    },
    {
        'slug': 'debugging-agents-with-traces', 'name': 'Debugging Agents with Traces', 'level': 'Advanced', 'category': 'Quality and governance',
        'summary': 'Debug agents from their traces \u2014 span trees that show every prompt, tool call, and handoff \u2014 to localize silent failures, loops, and cost blowups that plain logs never reveal.',
        'uses': ['Use when an agent finishes \u201csuccessfully\u201d but produces wrong results.', 'Use when multi-agent runs fail somewhere in the middle and nobody knows where.', 'Use when runaway loops burn tokens without raising a single error.'],
        'capabilities': ['Trace instrumentation', 'Span-tree reading', 'Loop detection', 'First-divergence analysis', 'Replay debugging'],
        'workflow': ['Instrument the agent once with an open standard (OpenTelemetry semantic conventions for GenAI) so traces survive framework and vendor changes.', 'Capture inputs, outputs, token counts, latency, and cost on every span \u2014 with secrets and personal data masked before storage.', 'On a bad run, read the trace top-down and find the first span whose output diverges from intent; everything downstream of it is symptom, not cause.', 'Check four signals on every incident: latency (p99, not the average), cost per run, error rate, and correctness \u2014 an agent can be fast, cheap, error-free, and wrong.', 'Detect loop tax by flagging repeated near-identical tool calls and runs whose cost is a multiple of the median run.', 'Fix at the divergent span, then add that trace to the regression set so the same failure stays fixed.'],
        'sources': [{'title': 'LLM Observability From Scratch \u2014 traces, spans, and silent failures (video)', 'url': 'https://www.youtube.com/watch?v=NH6wxVUlH10', 'license': 'YouTube standard license \u2014 concepts summarized, no content reproduced.'}, {'title': 'Langfuse repository', 'url': 'https://github.com/langfuse/langfuse', 'license': 'Open-source observability platform (MIT open-source core; see the repository LICENSE for current terms); this summary is derived, not copied.'}, {'title': 'OpenTelemetry GenAI semantic conventions', 'url': 'https://opentelemetry.io/docs/specs/semconv/gen-ai/', 'license': 'OpenTelemetry documentation (Apache-2.0 project); the conventions evolve \u2014 pin a version.'}],
        'archiveNote': 'Derived debugging workflow; traces are production data \u2014 apply retention and masking policies before storing or sharing them.', 'connectors': ['audit-log']
    },
])

skills = list({item['slug']: item for item in skills}.values())

connectors = [
    {'slug': 'web-search', 'name': 'Web search', 'credentialName': 'SEARCH_API_KEY', 'secretStored': False, 'access': 'Read-only search or browser connector', 'notes': 'Optional. Use a provider-specific server-side secret if a paid or authenticated search endpoint is selected.'},
    {'slug': 'document-store', 'name': 'Document store', 'credentialName': 'DOCUMENT_STORE_TOKEN', 'secretStored': False, 'access': 'Read-only document retrieval', 'notes': 'Use scoped access to the selected archive; do not expose the token to client-side JavaScript.'},
    {'slug': 'mcp-server', 'name': 'MCP server', 'credentialName': 'MCP_SERVER_TOKEN', 'secretStored': False, 'access': 'Defined per MCP server and tool', 'notes': 'Prefer separate credentials for read-only resources and mutating tools.'},
    {'slug': 'secrets-vault', 'name': 'Secrets vault', 'credentialName': 'VAULT_REFERENCE', 'secretStored': False, 'access': 'Runtime lookup by secret name', 'notes': 'The archive should store only a vault reference and scope, never the secret value.'},
    {'slug': 'audit-log', 'name': 'Audit log', 'credentialName': 'AUDIT_LOG_TOKEN', 'secretStored': False, 'access': 'Append-only security and tool events', 'notes': 'Mask credentials and personal data in logs.'},
    {'slug': 'provider-api', 'name': 'Provider API', 'credentialName': 'PROVIDER_API_KEY', 'secretStored': False, 'access': 'Provider-specific least-privilege scope', 'notes': 'Use a restricted key, server-side storage, rotation, revocation, and request monitoring.'},
]

catalog = {
    'name': '20/20 AI Skills Archive',
    'version': '2026-10-16',
    'description': 'Curated derived skills from free public courses and documentation. Source links and license notes are preserved; source course text is not copied wholesale.',
    'securityRule': 'API keys are credentials, not skills. This archive stores credential names and connector requirements only; it never stores secret key values.',
    'skills': skills,
}
(PUBLIC / 'skills.json').write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
(PUBLIC / 'connectors.json').write_text(json.dumps({'name': '20/20 Connector Catalog', 'version': '2026-10-16', 'securityRule': catalog['securityRule'], 'connectors': connectors}, indent=2, ensure_ascii=False))

for skill in skills:
    lines = [
        '---', f"name: {skill['slug']}", f"description: {skill['summary']} Use when the task matches the listed use cases.", '---', '',
        f"# {skill['name']}", '',
        '> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.', '',
        f"**Level:** {skill['level']}  ", f"**Category:** {skill['category']}", '',
        '## Purpose', '', skill['summary'], '',
        '## Use when', '', *[f'- {item}' for item in skill['uses']], '',
        '## Capabilities', '', *[f'- {item}' for item in skill['capabilities']], '',
        '## Workflow', '', *[f'{i + 1}. {item}' for i, item in enumerate(skill['workflow'])], '',
        '## Connector references', '',
        *([f'- `{item}`' for item in skill['connectors']] or ['- None required.']), '',
        '## Provenance and licensing', '', skill['archiveNote'], '',
    ]
    for source in skill['sources']:
        lines.append(f"- [{source['title']}]({source['url']}) — {source['license']}")
    (SKILL_DIR / f"{skill['slug']}.md").write_text('\n'.join(lines) + '\n')

print(f'Generated {len(skills)} skills and {len(connectors)} connector specifications')
