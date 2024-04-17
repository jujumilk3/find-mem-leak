# find-mem-leak

## Commands

### Docker

```bash
docker build -t find-mem-leak .
docker run  find-mem-leak -p 8000:8000
```

### Memray

```bash
memray run main.py  # run main.py with creating a memory snapshot (memray-main.py.15781.bin)
memray flamegraph memray-main.py.15781.bin  # create a flamegraph from the memory snapshot
memray run --live main.py
```
