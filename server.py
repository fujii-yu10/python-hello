import chainlit as cl

@cl.on_message
async def main(message: str):
    # ここにカスタムロジックを記述します

    # ユーザーへの応答を送信
    await cl.Message(
        content=f"受信: {message}",
    ).send()
