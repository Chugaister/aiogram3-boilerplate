from enum import Enum
from typing import List, Optional, Union

from aiogram import Bot
from aiogram.client.default import Default
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import (ForceReply, InlineKeyboardMarkup, InputFile,
                           LinkPreviewOptions, Message, MessageEntity,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           ReplyParameters)


class FileType(Enum):
    photo = "photo"
    video = "video"
    animation = "animation"


class CustomBot(Bot):

    async def send_message(
            self,
            chat_id: Union[int, str],
            text: str,
            message_thread_id: Optional[int] = None,
            parse_mode: Optional[Union[str, Default]] = Default("parse_mode"),
            entities: Optional[List[MessageEntity]] = None,
            link_preview_options: Optional[Union[LinkPreviewOptions, Default]] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[Union[bool, Default]] = Default("protect_content"),
            reply_parameters: Optional[ReplyParameters] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None,
            allow_sending_without_reply: Optional[bool] = None,
            disable_web_page_preview: Optional[Union[bool, Default]] = Default(
                "link_preview_is_disabled"
            ),
            reply_to_message_id: Optional[int] = None,
            request_timeout: Optional[int] = None,
            message_id_to_edit: Optional[int] = None,
            message_id_to_resend: Optional[int] = None
    ) -> Message:
        if message_id_to_edit:
            msg = await self.edit_message_text(
                text=text,
                chat_id=chat_id,
                message_id=message_id_to_edit,
                parse_mode=parse_mode,
                entities=entities,
                link_preview_options=link_preview_options,
                reply_markup=reply_markup,
                disable_web_page_preview=disable_web_page_preview
            )
            return msg
        if message_id_to_resend:
            await self.delete_message(
                chat_id=chat_id,
                message_id=message_id_to_resend,
                request_timeout=request_timeout
            )
        msg = await super().send_message(
            chat_id=chat_id,
            text=text,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            allow_sending_without_reply=allow_sending_without_reply,
            disable_web_page_preview=disable_web_page_preview,
            reply_to_message_id=reply_to_message_id,
        )
        return msg

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[Union[str, Default]] = Default("parse_mode"),
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[Union[bool, Default]] = Default(
            "show_caption_above_media"
        ),
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[Union[bool, Default]] = Default("protect_content"),
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        request_timeout: Optional[int] = None,
        message_id_to_resend: Optional[int] = None
    ) -> Message:
        if message_id_to_resend:
            await self.delete_message(
                chat_id=chat_id,
                message_id=message_id_to_resend,
                request_timeout=request_timeout
            )
        msg = await super().send_photo(
            chat_id=chat_id,
            photo=photo,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_to_message_id=reply_to_message_id,
            request_timeout=request_timeout
        )
        return msg

    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[InputFile] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[Union[str, Default]] = Default("parse_mode"),
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[Union[bool, Default]] = Default(
            "show_caption_above_media"
        ),
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[Union[bool, Default]] = Default("protect_content"),
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        request_timeout: Optional[int] = None,
        message_id_to_resend: Optional[int] = None
    ) -> Message:
        if message_id_to_resend:
            await self.delete_message(
                chat_id=chat_id,
                message_id=message_id_to_resend,
                request_timeout=request_timeout
            )
        msg = await super().send_video(
            chat_id=chat_id,
            video=video,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_to_message_id=reply_to_message_id,
            request_timeout=request_timeout
        )
        return msg

    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[InputFile] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[Union[str, Default]] = Default("parse_mode"),
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[Union[bool, Default]] = Default(
            "show_caption_above_media"
        ),
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[Union[bool, Default]] = Default("protect_content"),
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        request_timeout: Optional[int] = None,
        message_id_to_resend: Optional[int] = None
    ) -> Message:
        if message_id_to_resend:
            await self.delete_message(
                chat_id=chat_id,
                message_id=message_id_to_resend,
                request_timeout=request_timeout
            )
        msg = await super().send_animation(
            chat_id=chat_id,
            animation=animation,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_to_message_id=reply_to_message_id,
            request_timeout=request_timeout
        )
        return msg

    async def send_media(
            self,
            chat_id: int,
            text: Optional[str] = None,
            file_id: Optional[str] = None,
            file_type: Optional[FileType] = None,
            reply_markup: Optional[
                Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
            ] = None,
            message_id_to_edit: Optional[int] = None,
            message_id_to_resend: Optional[int] = None
    ) -> Message:
        if file_type == file_type.photo:
            msg = await self.send_photo(
                chat_id=chat_id,
                photo=file_id,
                caption=text,
                reply_markup=reply_markup,
                message_id_to_resend=message_id_to_resend
            )
        elif file_type == file_type.video:
            msg = await self.send_video(
                chat_id=chat_id,
                video=file_id,
                caption=text,
                reply_markup=reply_markup,
                message_id_to_resend=message_id_to_resend
            )
        elif file_type == file_type.animation:
            msg = await self.send_animation(
                chat_id=chat_id,
                animation=file_id,
                caption=text,
                reply_markup=reply_markup,
                message_id_to_resend=message_id_to_resend
            )
        elif text:
            msg = await self.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=reply_markup,
                message_id_to_resend=message_id_to_resend,
                message_id_to_edit=message_id_to_edit
            )
        else:
            raise ValueError(
                "CustomBot.send_media requires one of text, photo, " +
                "video or animation id and their combinations with text"
            )
        return msg

    async def safe_delete_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        request_timeout: Optional[int] = None,
    ) -> bool:
        try:
            return await super().delete_message(
                chat_id,
                message_id,
                request_timeout
            )
        except TelegramBadRequest:
            return False

    async def safe_answer_callback_query(
            self,
            callback_query_id: str,
            text: Optional[str] = None,
            show_alert: Optional[bool] = None,
            url: Optional[str] = None,
            cache_time: Optional[int] = None,
            request_timeout: Optional[int] = None,
    ) -> bool:
        try:
            return await super().answer_callback_query(
                    callback_query_id,
                    text,
                    show_alert,
                    url,
                    cache_time,
                    request_timeout
            )
        except TelegramBadRequest:
            return False
