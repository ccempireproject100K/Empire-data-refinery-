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




skills = list({item['slug']: item for item in skills}.values())[:20]

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
    'version': '2026-10-15',
    'description': 'Curated derived skills from free public courses and documentation. Source links and license notes are preserved; source course text is not copied wholesale.',
    'securityRule': 'API keys are credentials, not skills. This archive stores credential names and connector requirements only; it never stores secret key values.',
    'skills': skills,
}
(PUBLIC / 'skills.json').write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
(PUBLIC / 'connectors.json').write_text(json.dumps({'name': '20/20 Connector Catalog', 'version': '2026-10-15', 'securityRule': catalog['securityRule'], 'connectors': connectors}, indent=2, ensure_ascii=False))

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
