import asyncio

import langchain_openai
import pytest
from langchain.prompts import PromptTemplate

from opik.integrations.langchain.opik_tracer import OpikTracer

from ...testlib import (
    ANY_BUT_NONE,
    ANY_DICT,
    ANY_STRING,
    SpanModel,
    TraceModel,
    assert_equal,
)


@pytest.mark.parametrize(
    "llm_model, expected_input_prompt, stream_usage",
    [
        (
            langchain_openai.OpenAI,
            "Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris.",
            False,
        ),
        (
            langchain_openai.ChatOpenAI,
            "Human: Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris.",
            False,
        ),
        (
            langchain_openai.ChatOpenAI,
            "Human: Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris.",
            True,
        ),
    ],
)
def test_langchain__openai_llm_is_used__token_usage_is_logged__happyflow(
    fake_backend,
    ensure_openai_configured,
    llm_model,
    expected_input_prompt,
    stream_usage,
):
    llm_args = {
        "max_tokens": 10,
        "name": "custom-openai-llm-name",
    }
    if stream_usage is True:
        llm_args["stream_usage"] = stream_usage

    llm = llm_model(**llm_args)

    template = "Given the title of play, write a synopsys for that. Title: {title}."

    prompt_template = PromptTemplate(input_variables=["title"], template=template)

    synopsis_chain = prompt_template | llm
    test_prompts = {"title": "Documentary about Bigfoot in Paris"}

    callback = OpikTracer(tags=["tag1", "tag2"], metadata={"a": "b"})
    synopsis_chain.invoke(input=test_prompts, config={"callbacks": [callback]})

    callback.flush()

    EXPECTED_TRACE_TREE = TraceModel(
        id=ANY_BUT_NONE,
        name="RunnableSequence",
        input={"title": "Documentary about Bigfoot in Paris"},
        output=ANY_BUT_NONE,
        tags=["tag1", "tag2"],
        metadata={"a": "b"},
        start_time=ANY_BUT_NONE,
        end_time=ANY_BUT_NONE,
        spans=[
            SpanModel(
                id=ANY_BUT_NONE,
                name="RunnableSequence",
                input={"title": "Documentary about Bigfoot in Paris"},
                output=ANY_BUT_NONE,
                tags=["tag1", "tag2"],
                metadata={"a": "b"},
                start_time=ANY_BUT_NONE,
                end_time=ANY_BUT_NONE,
                spans=[
                    SpanModel(
                        id=ANY_BUT_NONE,
                        type="tool",
                        name="PromptTemplate",
                        input={"title": "Documentary about Bigfoot in Paris"},
                        output={"output": ANY_BUT_NONE},
                        metadata={},
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        spans=[],
                    ),
                    SpanModel(
                        id=ANY_BUT_NONE,
                        type="llm",
                        name="custom-openai-llm-name",
                        input={"prompts": [expected_input_prompt]},
                        output=ANY_BUT_NONE,
                        metadata=ANY_BUT_NONE,
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        usage={
                            "completion_tokens": ANY_BUT_NONE,
                            "prompt_tokens": ANY_BUT_NONE,
                            "total_tokens": ANY_BUT_NONE,
                        },
                        spans=[],
                        provider="openai",
                        model=ANY_STRING(startswith="gpt-3.5-turbo"),
                    ),
                ],
            )
        ],
    )

    assert len(fake_backend.trace_trees) == 1
    assert len(callback.created_traces()) == 1
    assert_equal(EXPECTED_TRACE_TREE, fake_backend.trace_trees[0])


def test_langchain__openai_llm_is_used__streaming_mode__token_usage_is_logged__happyflow(
    fake_backend,
    ensure_openai_configured,
):
    expected_input_prompt = "Human: Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris."

    callback = OpikTracer(
        tags=["tag3", "tag4"],
        metadata={"c": "d"},
    )

    model = langchain_openai.ChatOpenAI(
        max_tokens=10,
        name="custom-openai-llm-name",
        callbacks=[callback],
        # THIS PARAM IS VERY IMPORTANT!
        # if it is explicitly set to True - token usage data will be available
        stream_usage=True,
    )

    chunks = []
    for chunk in model.stream(
        "Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris."
    ):
        chunks.append(chunk)

    callback.flush()

    EXPECTED_TRACE_TREE = TraceModel(
        id=ANY_BUT_NONE,
        name="custom-openai-llm-name",
        input={"prompts": [expected_input_prompt]},
        output={
            "generations": ANY_BUT_NONE,
            "llm_output": None,
            "run": None,
            "type": "LLMResult",
        },
        tags=["tag3", "tag4"],
        metadata={
            "c": "d",
            "ls_max_tokens": 10,
            "ls_model_name": "gpt-3.5-turbo",
            "ls_model_type": "chat",
            "ls_provider": "openai",
            "ls_temperature": None,
        },
        start_time=ANY_BUT_NONE,
        end_time=ANY_BUT_NONE,
        spans=[
            SpanModel(
                id=ANY_BUT_NONE,
                name="custom-openai-llm-name",
                input={"prompts": [expected_input_prompt]},
                output=ANY_BUT_NONE,
                tags=["tag3", "tag4"],
                metadata={
                    "c": "d",
                    "ls_max_tokens": 10,
                    "ls_model_name": "gpt-3.5-turbo",
                    "ls_model_type": "chat",
                    "ls_provider": "openai",
                    "ls_temperature": None,
                    "usage": {
                        "completion_tokens": ANY_BUT_NONE,
                        "input_token_details": {
                            "audio": ANY_BUT_NONE,
                            "cache_read": ANY_BUT_NONE,
                        },
                        "input_tokens": ANY_BUT_NONE,
                        "output_token_details": {
                            "audio": ANY_BUT_NONE,
                            "reasoning": ANY_BUT_NONE,
                        },
                        "output_tokens": ANY_BUT_NONE,
                        "prompt_tokens": ANY_BUT_NONE,
                        "total_tokens": ANY_BUT_NONE,
                    },
                },
                start_time=ANY_BUT_NONE,
                end_time=ANY_BUT_NONE,
                spans=[],
                type="llm",
                model=ANY_STRING(startswith="gpt-3.5-turbo"),
                provider="openai",
                usage={
                    "completion_tokens": ANY_BUT_NONE,
                    "prompt_tokens": ANY_BUT_NONE,
                    "total_tokens": ANY_BUT_NONE,
                },
            )
        ],
    )

    assert len(fake_backend.trace_trees) == 1
    assert len(callback.created_traces()) == 1
    assert_equal(EXPECTED_TRACE_TREE, fake_backend.trace_trees[0])


def test_langchain__openai_llm_is_used__async_astream__no_token_usage_is_logged__happyflow(
    fake_backend,
    ensure_openai_configured,
):
    """
    In `astream` mode, the `token_usage` is not provided by langchain.
    For trace `input` always will be = {"input": ""}
    """
    callback = OpikTracer(
        tags=["tag3", "tag4"],
        metadata={"c": "d"},
    )

    model = langchain_openai.ChatOpenAI(
        model="gpt-4o",
        max_tokens=10,
        name="custom-openai-llm-name",
        callbacks=[callback],
        # `stream_usage` param is VERY IMPORTANT!
        # if it is explicitly set to True - token usage data will be available
        # "stream_usage": True,
    )

    template = "Given the title of play, write a synopsys for that. Title: {title}."
    prompt_template = PromptTemplate(input_variables=["title"], template=template)

    chain = prompt_template | model

    async def stream_generator(chain, inputs):
        async for chunk in chain.astream(inputs, config={"callbacks": [callback]}):
            yield chunk

    async def invoke_generator(chain, inputs):
        async for chunk in stream_generator(chain, inputs):
            print(chunk)

    inputs = {"title": "The Hobbit"}

    asyncio.run(invoke_generator(chain, inputs))

    callback.flush()

    EXPECTED_TRACE_TREE = TraceModel(
        id=ANY_BUT_NONE,
        name="RunnableSequence",
        input={"input": ""},
        output=ANY_DICT,
        tags=["tag3", "tag4"],
        metadata={
            "c": "d",
        },
        start_time=ANY_BUT_NONE,
        end_time=ANY_BUT_NONE,
        spans=[
            SpanModel(
                id=ANY_BUT_NONE,
                name="RunnableSequence",
                input={"input": ""},
                output=ANY_BUT_NONE,
                tags=["tag3", "tag4"],
                metadata={
                    "c": "d",
                },
                start_time=ANY_BUT_NONE,
                end_time=ANY_BUT_NONE,
                type="general",
                model=None,
                provider=None,
                usage=None,
                spans=[
                    SpanModel(
                        id=ANY_BUT_NONE,
                        name="PromptTemplate",
                        input={"title": "The Hobbit"},
                        output=ANY_BUT_NONE,
                        tags=None,
                        metadata={},
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        type="tool",
                        model=None,
                        provider=None,
                        usage=None,
                        spans=[],
                    ),
                    SpanModel(
                        id=ANY_BUT_NONE,
                        name="custom-openai-llm-name",
                        input={
                            "prompts": [
                                "Human: Given the title of play, write a synopsys for that. Title: The Hobbit."
                            ]
                        },
                        output=ANY_BUT_NONE,
                        tags=None,
                        metadata=ANY_DICT,
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        type="llm",
                        model=ANY_STRING(startswith="gpt-4o"),
                        provider="openai",
                        usage=None,
                        spans=[],
                    ),
                ],
            )
        ],
    )

    assert len(fake_backend.trace_trees) == 1
    assert len(callback.created_traces()) == 1
    assert_equal(EXPECTED_TRACE_TREE, fake_backend.trace_trees[0])


def test_langchain__openai_llm_is_used__error_occurred_during_openai_call__error_info_is_logged(
    fake_backend,
):
    llm = langchain_openai.OpenAI(
        max_tokens=10, name="custom-openai-llm-name", api_key="incorrect-api-key"
    )

    template = "Given the title of play, write a synopsys for that. Title: {title}."

    prompt_template = PromptTemplate(input_variables=["title"], template=template)

    synopsis_chain = prompt_template | llm
    test_prompts = {"title": "Documentary about Bigfoot in Paris"}

    callback = OpikTracer(tags=["tag1", "tag2"], metadata={"a": "b"})
    with pytest.raises(Exception):
        synopsis_chain.invoke(input=test_prompts, config={"callbacks": [callback]})

    callback.flush()

    EXPECTED_TRACE_TREE = TraceModel(
        id=ANY_BUT_NONE,
        name="RunnableSequence",
        input={"title": "Documentary about Bigfoot in Paris"},
        output=None,
        tags=["tag1", "tag2"],
        metadata={"a": "b"},
        start_time=ANY_BUT_NONE,
        end_time=ANY_BUT_NONE,
        error_info={
            "exception_type": ANY_STRING(),
            "traceback": ANY_STRING(),
        },
        spans=[
            SpanModel(
                id=ANY_BUT_NONE,
                name="RunnableSequence",
                input={"title": "Documentary about Bigfoot in Paris"},
                output=None,
                tags=["tag1", "tag2"],
                metadata={"a": "b"},
                start_time=ANY_BUT_NONE,
                end_time=ANY_BUT_NONE,
                error_info={
                    "exception_type": ANY_STRING(),
                    "traceback": ANY_STRING(),
                },
                spans=[
                    SpanModel(
                        id=ANY_BUT_NONE,
                        type="tool",
                        name="PromptTemplate",
                        input={"title": "Documentary about Bigfoot in Paris"},
                        output={"output": ANY_BUT_NONE},
                        metadata={},
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        spans=[],
                    ),
                    SpanModel(
                        id=ANY_BUT_NONE,
                        type="llm",
                        name="custom-openai-llm-name",
                        input={
                            "prompts": [
                                "Given the title of play, write a synopsys for that. Title: Documentary about Bigfoot in Paris."
                            ]
                        },
                        output=None,
                        metadata=ANY_BUT_NONE,
                        start_time=ANY_BUT_NONE,
                        end_time=ANY_BUT_NONE,
                        usage=None,
                        error_info={
                            "exception_type": ANY_STRING(),
                            "traceback": ANY_STRING(),
                        },
                        spans=[],
                    ),
                ],
            )
        ],
    )

    assert len(fake_backend.trace_trees) == 1
    assert len(callback.created_traces()) == 1
    assert_equal(EXPECTED_TRACE_TREE, fake_backend.trace_trees[0])
