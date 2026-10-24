# Flowise Tool Agent Not Using Retriever Tool

If there are **no errors** and the agent responds normally but **never calls the Retriever Tool**, then the problem is usually **agent/tool configuration**, not Pinecone.

## 1. Verify the Tool Is Actually Available to the Agent

In the Tool Agent node, inspect the available tools list.

You should see something like:

```text
Tools:
- cis-retriever
```

If the tool does not appear there, the connection exists visually but is not registered with the agent.

---

## 2. Improve the Tool Description

Agents decide whether to use a tool based heavily on its name and description.

### Bad

```text
Name: cis-retriever
Description: Retriever
```

### Better

```text
Name: cis-retriever

Description:
Search CIS benchmark documentation, Windows security policies,
password policies, account lockout policies, audit policies,
and security configuration guidance.

Use this tool whenever the answer may be contained in CIS documents.
```

Many times the agent simply doesn't realize the tool is relevant.

---

## 3. Force a Retrieval-Oriented System Prompt

If your Tool Agent has a system prompt, add something like:

```text
When answering questions about CIS benchmarks,
Windows security settings,
password policies,
security controls,
or configuration standards,
ALWAYS search the cis-retriever tool before answering.

Do not rely on prior knowledge when the tool may contain relevant information.
```

Without this, GPT often answers from its own knowledge.

---

## 4. Test With an Impossible Question

Ask:

```text
What is section 2.3.7.11 of our CIS benchmark?
```

or

```text
Quote the password policy from our uploaded document.
```

If the agent still answers without tool usage, it is ignoring the tool.

If it calls the tool, the issue is that your normal questions are too generic and the model prefers its own knowledge.

---

## 5. Check Tool Choice / Function Calling Settings

Depending on your Flowise version:

- Tool Choice = Auto
- Tool Choice = Required
- Function Calling enabled

For debugging, if available, set:

```text
Tool Choice = Required
```

Then ask:

```text
password policies in Windows 11
```

The agent should be forced to invoke a tool.

---

## 6. Turn On Verbose / Execution Logs

In Flowise:

```text
Settings
→ Verbose
→ Debug
```

Look for traces such as:

```text
Agent deciding...
Tool selected: cis-retriever
```

or

```text
No tool selected
```

This immediately tells you whether the agent considered the tool.

---

## 7. Verify Retrieval Independently

Before involving the agent, test the Retriever Tool directly.

Query:

```text
password policies in Windows 11
```

Expected:

```text
Retrieved 3 documents...
```

If retrieval returns nothing, the agent may correctly decide not to use it.

---

## 8. Check the Model

### Generally Reliable

- GPT-4o
- GPT-4.1
- GPT-4 Turbo
- Claude Sonnet

### Less Reliable for Tool Calling

- Small local models
- Older Llama variants
- Some Gemini configurations

---

## Quick Diagnostic

Ask the agent:

```text
Use the cis-retriever tool and tell me what documents mention password policies.
```

Then inspect the execution trace.

If the tool still isn't called, the issue is likely:

- Tool not actually registered with the agent
- Function/tool calling disabled
- Flowise version-specific bug

### Information Needed for Further Debugging

1. Flowise version
2. Agent type (Tool Agent, OpenAI Functions Agent, ReAct Agent, Agentflow, etc.)
3. Model being used (GPT-4o, Azure GPT-4o, Gemini, Ollama, etc.)
