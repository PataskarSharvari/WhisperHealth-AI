#VoiceBot UI with Enhanced Gradio Interface
import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_doctor import text_to_speech_with_gtts
from voice_of_the_patient import record_audio, transcribe_with_groq

from dotenv import load_dotenv
load_dotenv()

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath, progress=gr.Progress()):
    try:
        progress(0.1, desc="Processing audio...")
        
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
        
        progress(0.4, desc="Analyzing image...")
        
        if image_filepath:
            encoded_img = encode_image(image_filepath)
            progress(0.6, desc="Getting medical analysis...")
            doctor_response = analyze_image_with_query(
                query=system_prompt + speech_to_text_output,
                encoded_image=encoded_img,
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        else:
            doctor_response = "Please provide an image for me to analyze your medical concern."

        progress(0.8, desc="Generating voice response...")
        # Generate voice
        audio_path = text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3")
        
        progress(1.0, desc="Complete!")
        return speech_to_text_output, doctor_response, audio_path

    except Exception as e:
        print(f"🔥 Error in process_inputs(): {e}")
        return "Error in processing", f"I apologize, but I encountered an error: {str(e)}", None

def clear_all():
    return None, None, "", "", None

# Custom CSS for medical theme
custom_css = """
/* Main container styling */
.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

/* Header styling */
.main-header {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Input section styling */
.input-section {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(15px);
    border-radius: 15px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Output section styling */
.output-section {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(15px);
    border-radius: 15px;
    padding: 25px;
    margin: 15px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Button styling */
.medical-button {
    background: linear-gradient(45deg, #4CAF50, #45a049) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 12px 30px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3) !important;
    transition: all 0.3s ease !important;
}

.medical-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4) !important;
}

.clear-button {
    background: linear-gradient(45deg, #ff6b6b, #ee5a5a) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 12px 30px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    transition: all 0.3s ease !important;
}

.clear-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4) !important;
}

/* Audio and image upload styling */
.gr-file-upload, .gr-audio {
    border: 2px dashed #4CAF50 !important;
    border-radius: 15px !important;
    background: rgba(255, 255, 255, 0.8) !important;
    padding: 20px !important;
    transition: all 0.3s ease !important;
}

.gr-file-upload:hover, .gr-audio:hover {
    border-color: #45a049 !important;
    background: rgba(255, 255, 255, 0.9) !important;
    transform: translateY(-2px) !important;
}

/* Textbox styling */
.gr-textbox {
    border-radius: 10px !important;
    border: 1px solid #e0e0e0 !important;
    background: rgba(255, 255, 255, 0.9) !important;
    font-size: 14px !important;
    line-height: 1.6 !important;
}

/* Title styling */
.gr-interface h1 {
    color: #1a1a1a !important;
    text-align: center !important;
    font-size: 2.5em !important;
    font-weight: 700 !important;
    margin-bottom: 10px !important;
    text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.3) !important;
}

/* Description styling */
.gr-interface .gr-form > .gr-box:first-child p {
    color: #2c2c2c !important;
    text-align: center !important;
    font-size: 1.2em !important;
    font-weight: 400 !important;
    margin-bottom: 20px !important;
}

/* Labels styling */
.gr-interface label {
    color: #2c3e50 !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    margin-bottom: 8px !important;
}

/* Progress bar styling */
.gr-progress {
    background: linear-gradient(90deg, #4CAF50, #45a049) !important;
    border-radius: 10px !important;
}

/* Medical icons and emojis */
.medical-icon {
    font-size: 2em;
    margin: 0 10px;
    vertical-align: middle;
}

/* Responsive design */
@media (max-width: 768px) {
    .gradio-container {
        padding: 10px !important;
    }
    
    .main-header, .input-section, .output-section {
        padding: 15px !important;
        margin: 10px 0 !important;
    }
    
    .gr-interface h1 {
        font-size: 1.8em !important;
    }
}
"""

# Create the enhanced interface using Blocks for better control
with gr.Blocks(
    css=custom_css,
    title="🏥 AI Medical Assistant",
    theme=gr.themes.Soft(
        primary_hue="green",
        secondary_hue="blue",
        neutral_hue="slate",
        font=gr.themes.GoogleFont("Inter")
    )
) as demo:
    
    # Header Section
    gr.HTML("""
    <div class="main-header" style="padding: 20px; background: rgba(255,255,255,0.95); border-radius: 15px;">
        <style>
            .main-header * {
                color: #000000 !important;
                text-align: center !important;
            }
            .main-header .disclaimer {
                color: #d32f2f !important;
                font-size: 14px;
                margin-top: 10px;
                font-weight: 500;
                background: rgba(255, 235, 238, 0.8);
                padding: 8px;
                border-radius: 8px;
                display: inline-block;
            }
        </style>
        <h1 style="text-shadow: 1px 1px 2px rgba(255,255,255,0.5); font-weight: 700;">🏥 WHISPERHEALTH - Your AI Medical Assistant</h1>
        <p style="font-size: 18px; margin: 5px 0; font-weight: 500;">
            🩺 Upload medical images and describe symptoms for AI-powered preliminary analysis
        </p>
        <p class="disclaimer">
            ⚠️ <em>This is for educational purposes only. Always consult with a real healthcare professional.</em>
        </p>
    </div>
""")

   
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.HTML("""
                <div class="input-section">
                    <h3 style="color: #2c3e50; margin-bottom: 20px; text-align: center;">
                        📋 Patient Input
                    </h3>
                </div>
            """)
            
            # Audio input with enhanced styling
            audio_input = gr.Audio(
                type="filepath",
                label="🎤 Record Your Voice / Describe Symptoms",
                interactive=True,
                elem_classes=["medical-input"]
            )
            
            # Image input with enhanced styling
            image_input = gr.Image(
                type="filepath",
                label="📸 Upload Medical Image (X-ray, Scan, Photo, etc.)",
                elem_classes=["medical-input"]
            )
            
            # Control buttons
            with gr.Row():
                analyze_btn = gr.Button(
                    "🔍 Analyze & Diagnose",
                    variant="primary",
                    elem_classes=["medical-button"],
                    scale=2
                )
                clear_btn = gr.Button(
                    "🗑️ Clear All",
                    variant="secondary",
                    elem_classes=["clear-button"],
                    scale=1
                )
        
        with gr.Column(scale=1):
            gr.HTML("""
                <div class="output-section">
                    <h3 style="color: #2c3e50; margin-bottom: 20px; text-align: center;">
                        👨‍⚕️ Medical Analysis
                    </h3>
                </div>
            """)
            
            # Output components with enhanced styling
            transcription_output = gr.Textbox(
                label="📝 Your Voice Transcription",
                interactive=False,
                lines=3,
                elem_classes=["output-textbox"]
            )
            
            analysis_output = gr.Textbox(
                label="🏥 Doctor's Analysis & Recommendations",
                interactive=False,
                lines=5,
                elem_classes=["output-textbox"]
            )
            
            audio_output = gr.Audio(
                label="🔊 Listen to Doctor's Response",
                type="filepath",
                interactive=False,
                elem_classes=["output-audio"]
            )
    
    # Information section
    gr.HTML("""
    <div style="background: rgba(255, 255, 255, 0.95); border-radius: 15px; padding: 20px; margin-top: 20px; border-left: 5px solid #4CAF50; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <style>
            .instruction-box * {
                color: #000000 !important;
            }
            .instruction-box .disclaimer {
                color: #d32f2f !important;
                background: rgba(255,235,238,0.8);
                padding: 10px;
                border-radius: 8px;
                font-weight: 600;
            }
        </style>
        <div class="instruction-box">
            <h4 style="margin-bottom: 15px; font-weight: 600;">📋 How to Use:</h4>
            <ul style="line-height: 1.8; font-weight: 400;">
                <li><strong>Step 1:</strong> 🎤 Record your voice describing your symptoms or medical concerns</li>
                <li><strong>Step 2:</strong> 📸 Upload a relevant medical image (X-ray, photo, scan, etc.)</li>
                <li><strong>Step 3:</strong> 🔍 Click "Analyze & Diagnose" to get AI-powered medical insights</li>
                <li><strong>Step 4:</strong> 👂 Listen to the audio response and read the written analysis</li>
            </ul>
            <p class="disclaimer">
                ⚠️ Disclaimer: This AI assistant is for educational and informational purposes only.
                It should not replace professional medical advice, diagnosis, or treatment.
            </p>
        </div>
    </div>
""")


    
    # Event handlers
    analyze_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[transcription_output, analysis_output, audio_output],
        show_progress=True
    )
    
    clear_btn.click(
        fn=clear_all,
        outputs=[audio_input, image_input, transcription_output, analysis_output, audio_output]
    )

# Launch the enhanced interface
if __name__ == "__main__":
    demo.launch(
        debug=True,
        share=True,  # This creates a public link you can access
        inbrowser=True,  # Automatically opens in browser
        show_error=True
    )