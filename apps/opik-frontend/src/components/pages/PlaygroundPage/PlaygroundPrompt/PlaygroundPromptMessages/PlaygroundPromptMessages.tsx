import React, { useCallback } from "react";
// ALEX CHECK EXPORTS
import { arrayMove, verticalListSortingStrategy } from "@dnd-kit/sortable";

import { PlaygroundMessageType } from "@/types/playgroundPrompts";
import { generateDefaultPlaygroundPromptMessage } from "@/lib/playgroundPrompts";
import { SortableContext } from "@dnd-kit/sortable";
import {
  closestCenter,
  DndContext,
  MouseSensor,
  useSensor,
  useSensors,
} from "@dnd-kit/core";
import PlaygroundPromptMessage from "@/components/pages/PlaygroundPage/PlaygroundPrompt/PlaygroundPromptMessages/PlaygroundPromptMessage";
import type { DragEndEvent } from "@dnd-kit/core/dist/types";
import { keyBy } from "lodash";

interface PlaygroundPromptMessagesProps {
  messages: PlaygroundMessageType[];
  onChange: (messages: PlaygroundMessageType[]) => void;
}

const PlaygroundPromptMessages = ({
  messages,
  onChange,
}: PlaygroundPromptMessagesProps) => {
  const sensors = useSensors(
    useSensor(MouseSensor, {
      activationConstraint: {
        distance: 2,
      },
    }),
  );

  const handleDuplicateMessage = useCallback(
    (message: Partial<PlaygroundMessageType> = {}, position: number) => {
      const newMessage = generateDefaultPlaygroundPromptMessage(message);
      const newMessages = [...messages];

      newMessages.splice(position, 0, newMessage);

      onChange(newMessages);
    },
    [onChange, messages],
  );

  const handleRemoveMessage = useCallback(
    (messageId: string) => {
      onChange(messages.filter((m) => m.id !== messageId));
    },
    [onChange, messages],
  );

  const handleChangeMessage = useCallback(
    (messageId: string, changes: Partial<PlaygroundMessageType>) => {
      onChange(
        messages.map((m) => (m.id !== messageId ? m : { ...m, ...changes })),
      );
    },
    [onChange, messages],
  );

  // ALEX
  const handleDragEnd = useCallback(
    (event: DragEndEvent) => {
      const { active, over } = event;

      const messageMap = keyBy(messages, "id");
      const localOrder = messages.map((m) => m.id);

      if (over && active.id !== over.id) {
        const oldIndex = localOrder.indexOf(active.id as string);
        const newIndex = localOrder.indexOf(over.id as string);

        const newOrder = arrayMove(localOrder, oldIndex, newIndex);
        const newMessageOrder = newOrder.map(
          (messageId) => messageMap[messageId],
        );

        onChange(newMessageOrder);
      }
    },
    [onChange, messages],
  );

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCenter}
      onDragEnd={handleDragEnd}
    >
      <SortableContext items={messages} strategy={verticalListSortingStrategy}>
        <div className="flex flex-col gap-2">
          {/*ALEX check the functions*/}
          {messages.map((message, messageIdx) => (
            <PlaygroundPromptMessage
              key={message.id}
              hideRemoveButton={messages?.length === 1}
              hideDragButton={messages?.length === 1}
              onRemoveMessage={() => handleRemoveMessage(message.id)}
              onDuplicateMessage={() =>
                handleDuplicateMessage(message, messageIdx + 1)
              }
              onChangeMessage={(changes) =>
                handleChangeMessage(message.id, changes)
              }
              {...message}
            />
          ))}
        </div>
      </SortableContext>
    </DndContext>
  );
};

export default PlaygroundPromptMessages;
