from typing import List, Optional
import gradio
import onnxruntime

import main.globals as globals
from main.instances import clear_instances
import main.uis.choices as choices
from main.utils.device import encode_devices, decode_devices


PROCESS_MODE_DROPDOWN: Optional[gradio.Dropdown] = None
THREAD_SLIDER: Optional[gradio.Slider] = None
QUEUE_SLIDER: Optional[gradio.Slider] = None
OUTPUT_VIDEO_FPS_CHECKBOX: Optional[gradio.Checkbox] = None
DEVICE_CHECKBOX: Optional[gradio.CheckboxGroup] = None
DETECT_FACE_MODEL_DROPDOWN: Optional[gradio.Dropdown] = None
DETECT_SCORE_THRESHOLD_SLIDER: Optional[gradio.Slider] = None
DETECT_IOU_THRESHOLD_SLIDER: Optional[gradio.Slider] = None
ENHANCE_MODEL_DROPDOWN: Optional[gradio.Dropdown] = None
SWAP_MODEL_DROPDOWN: Optional[gradio.Dropdown] = None
EXECUTION_GROUP: Optional[gradio.Group] = None
VIDEO_GROUP: Optional[gradio.Group] = None
DETECT_GROUP: Optional[gradio.Group] = None
SWAP_GROUP: Optional[gradio.Group] = None


def update_process_mode(process_mode : str) -> gradio.Group:
    globals.process_mode = process_mode
    if process_mode == 'swap':
        return gradio.Group(visible = True)
    return gradio.Group(visible = False)


def update_thread(thread : int) -> None:
    globals.thread = thread


def update_queue(queue : int) -> None:
    globals.queue = queue


def update_device(device : List[str]) -> None:
    clear_instances()
    if not device:
        device = encode_devices(onnxruntime.get_available_providers())
    globals.device = decode_devices(device)


def update_output_video_fps(keep_fps : float) -> None:
    if keep_fps:
        globals.keep_fps = True
    else:
        globals.keep_fps = False


def update_detect_face_model(detect_face_model : str) -> None:
    globals.detect_face_model = detect_face_model


def update_detect_score_threshold(score_threshold : float) -> None:
    globals.score_threshold = score_threshold


def update_detect_iou_threshold(iou_threshold : float) -> None:
    globals.iou_threshold = iou_threshold


def update_enhance_model(enhance_model : str) -> None:
    globals.enhance_face_model = enhance_model


def update_swap_model(swap_model : str) -> None:
    globals.swap_face_model = swap_model


def render():
    global PROCESS_MODE_DROPDOWN
    global THREAD_SLIDER
    global QUEUE_SLIDER
    global OUTPUT_VIDEO_FPS_CHECKBOX
    global DEVICE_CHECKBOX
    global DETECT_FACE_MODEL_DROPDOWN
    global DETECT_SCORE_THRESHOLD_SLIDER
    global DETECT_IOU_THRESHOLD_SLIDER
    global ENHANCE_MODEL_DROPDOWN
    global SWAP_MODEL_DROPDOWN
    global EXECUTION_GROUP
    global VIDEO_GROUP
    global DETECT_GROUP
    global SWAP_GROUP

    PROCESS_MODE_DROPDOWN = gradio.Dropdown(choices = choices.process_mode, label='Process Mode', value = globals.process_mode)
    
    EXECUTION_GROUP = gradio.Group()
    with EXECUTION_GROUP:
        THREAD_SLIDER = gradio.Slider(minimum = 1, maximum = 100, step = 1, label = 'Thread', value = globals.thread)
        QUEUE_SLIDER = gradio.Slider(minimum = 1, maximum = 100, step = 1, label = 'Queue', value = globals.queue)
        DEVICE_CHECKBOX = gradio.CheckboxGroup(label = 'Device', value = encode_devices(globals.device), choices = encode_devices(onnxruntime.get_available_providers()))
    
    VIDEO_GROUP = gradio.Group()
    with VIDEO_GROUP:
        OUTPUT_VIDEO_FPS_CHECKBOX = gradio.Checkbox(label = 'Keep Video FPS', value = False)
    
    DETECT_GROUP = gradio.Group()
    with DETECT_GROUP:
        DETECT_FACE_MODEL_DROPDOWN = gradio.Dropdown(choices = choices.detect_face_model, label = 'Detect Face Model', value = globals.detect_face_model)
        DETECT_SCORE_THRESHOLD_SLIDER = gradio.Slider(minimum = 0.0, maximum = 1.0, label = 'Detect Score Threshold', value = globals.score_threshold)
        DETECT_IOU_THRESHOLD_SLIDER = gradio.Slider(minimum = 0.0, maximum = 1.0, label = 'Detect IoU Threshold', value = globals.iou_threshold)
    
    SWAP_GROUP = gradio.Group()
    with SWAP_GROUP:
        ENHANCE_MODEL_DROPDOWN = gradio.Dropdown(choices = choices.enhance_face_model, label = 'Enhance Face Model', value = globals.enhance_face_model)
        SWAP_MODEL_DROPDOWN = gradio.Dropdown(choices = choices.swap_face_model, label = 'Swap Face Model', value = globals.swap_face_model)


def listen():
    PROCESS_MODE_DROPDOWN.change(fn = update_process_mode, inputs = PROCESS_MODE_DROPDOWN, outputs = SWAP_GROUP)
    THREAD_SLIDER.change(fn = update_thread, inputs = THREAD_SLIDER)
    QUEUE_SLIDER.change(fn = update_queue, inputs = QUEUE_SLIDER)
    DEVICE_CHECKBOX.change(fn = update_device, inputs = DEVICE_CHECKBOX)
    OUTPUT_VIDEO_FPS_CHECKBOX.change(fn = update_output_video_fps, inputs = OUTPUT_VIDEO_FPS_CHECKBOX)
    DETECT_FACE_MODEL_DROPDOWN.change(fn = update_detect_face_model, inputs = DETECT_FACE_MODEL_DROPDOWN)
    DETECT_SCORE_THRESHOLD_SLIDER.change(fn = update_detect_score_threshold, inputs = DETECT_SCORE_THRESHOLD_SLIDER)
    DETECT_IOU_THRESHOLD_SLIDER.change(fn = update_detect_iou_threshold, inputs = DETECT_IOU_THRESHOLD_SLIDER)
    ENHANCE_MODEL_DROPDOWN.change(fn = update_enhance_model, inputs = ENHANCE_MODEL_DROPDOWN)
    SWAP_MODEL_DROPDOWN.change(fn = update_swap_model, inputs = SWAP_MODEL_DROPDOWN)