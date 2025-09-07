from flask import Flask, request, jsonify
import hashlib
from argon2.low_level import hash_secret, Type

app = Flask(__name__)

# -------------------------
# 해시 함수 구현
# -------------------------
def sha256_hex(text: str) -> str:
    """SHA-256 해시를 hex로 반환"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def argon2id_hash(
    text: str,
    salt: str,
    time_cost: int = 2,
    memory_cost_kib: int = 65536,  # 64 MiB
    parallelism: int = 1,
    hash_len: int = 32,
) -> str:
    """Argon2id 해시 (데모용)"""
    secret = text.encode("utf-8")
    salt_b = salt.encode("utf-8")
    return hash_secret(
        secret=secret,
        salt=salt_b,
        time_cost=int(time_cost),
        memory_cost=int(memory_cost_kib),
        parallelism=int(parallelism),
        hash_len=int(hash_len),
        type=Type.ID
    ).decode("utf-8")

# -------------------------
# API 엔드포인트
# -------------------------
@app.route("/api/hash", methods=["POST"])
def api_hash():
    try:
        data = request.get_json(force=True) or {}
        mode = (data.get("mode") or "sha256").lower()
        text = data.get("text", "")

        if not isinstance(text, str):
            return jsonify({"error": "text must be a string"}), 400

        if mode == "sha256":
            return jsonify({"mode": "sha256", "sha256_hex": sha256_hex(text)})

        elif mode == "argon2id":
            salt = data.get("salt") or "demo_salt"
            time_cost = data.get("time_cost", 2)
            memory_cost_kib = data.get("memory_cost_kib", 65536)
            parallelism = data.get("parallelism", 1)
            hash_len = data.get("hash_len", 32)
            result = argon2id_hash(text, salt, time_cost, memory_cost_kib, parallelism, hash_len)
            return jsonify({
                "mode": "argon2id",
                "argon2id": result,
                "params": {
                    "salt": salt,
                    "time_cost": int(time_cost),
                    "memory_cost_kib": int(memory_cost_kib),
                    "parallelism": int(parallelism),
                    "hash_len": int(hash_len),
                }
            })
        else:
            return jsonify({"error": "unsupported mode"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------
# 실행
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
